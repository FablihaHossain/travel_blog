from django.shortcuts import render, redirect
from .models import User, Entry, EntryImage
from django.http import Http404, HttpResponse
from .forms import LoginForm, RegistrationForm, NewEntryForm, EntryImageForm
from django.forms import modelformset_factory
from django.forms import formset_factory

# Basic Route for the Site
def index(request):
	# Getting all users
	users = User.objects.all()

	# Getting all entries
	entries = Entry.objects.all()

	# Getting all entry images
	images = EntryImage.objects.all()

	# Getting current name if logged in
	userId = request.session.get('user_id')
	if userId:
		theUser = User.objects.get(id = userId)
	else:
		theUser = None

	return render(request, 'index.html', {'users':users, 'entries':entries, 'images':images, 'theUser': theUser})

# Login Page
def login(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		loggedInUser = None
		if login_form.is_valid():
			try:
				# Validating user credentials
				loggedInUser = User.objects.get(username = request.POST['username'])
				if loggedInUser.password == request.POST['password']:
					# Updating the session details for the logged in user
					request.session['user_id'] = loggedInUser.id
					request.session['username'] = loggedInUser.username
					return redirect('/')
				else:
				# Error message and new login form if incorrect login
					message = 'Error! Invalid Log In... Please Try Again'
					new_form = LoginForm()
					return render(request, 'login.html', {'loginform':new_form, 'message':message})
			except User.DoesNotExist:
				# Exception raised if the user doesn't exist in the database
				raise Http404('Error! Username Does Not Exist')
	else: 	
		# Original Login Form
		form = LoginForm()
		return render(request, 'login.html', {'loginform':form})

def logout(request):
	try:
		# Clearing the session after user logs out
		del request.session['user_id']
		del request.session['username']
		return render(request, 'logout.html')
	except KeyError:
		pass
	return render(request, 'logout.html')

# Registration Page
def register(request):
	if request.method == 'POST':
		# getting all the current registration information
		updated_request = request.POST.copy()
		# updating the role of the user 
		updated_request.update({'role': 'G'})
		# putting all updated information into the role
		register_form = RegistrationForm(updated_request)

		# checking if registration form is valid
		if register_form.is_valid():
			# Creating new user and assign it the general user role
			new_user = register_form.save(commit=False)
			new_user.role = 'G'
			new_user.save()

			# Saving the New User
			register_form.save()
			# Redirecting to login page
			return redirect('/login')
	else:
		register_form = RegistrationForm()
		return render(request, 'registration.html', {'registrationform':register_form})

# The homepage will contain all entries
def homepage(request):
	# Redirect to login page if user not logged in
	if not request.session.get('username'):
		return redirect('/login')

	# Getting all entries
	entries = Entry.objects.order_by('-id')

	# Getting all entry images
	images = EntryImage.objects.all()

	# Getting all authors
	authors = User.objects.all()

	# Getting the list of users that submitted entries
	listOfAuthorNames = []
	for entry in entries:
		for auth in authors:
			if entry.author == auth:
				listOfAuthorNames.append(auth.name)

	# Getting list of initial images to act as cover images for the entry card
	listOfCoverImages = []
	for entry in entries:
		for img in images:
			if img.entry_id == entry.id:
				listOfCoverImages.append(img)
				break
	return render(request, 'homepage.html', {'entries':entries, 'data': zip(entries, listOfAuthorNames, listOfCoverImages)})

# Viewing Entries Individually Based on Entry ID
def viewEntry(request, entry_id):
	# Redirect to login page if user not logged in
	if not request.session.get('username'):
		return redirect('/login')

	try:
		# Getting the details of current entry based on given id
		entry = Entry.objects.get(id = entry_id)
		images = EntryImage.objects.all()

		# Getting the corresponding images of the entry
		currentImages = []
		for img in images:
			if img.entry_id == entry.id:
				currentImages.append(img)
	except Entry.DoesNotExist:
		# Error handling if the entry does not exist
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'viewEntry.html', {'entry':entry,'images':currentImages})

# New Entry Form Page
def newEntry(request):
	# Redirect to login page if user not logged in
	if not request.session.get('username'):
		return redirect('/login')

	# Creating new image form for the new entry
	ImageFormSet = modelformset_factory(EntryImage, form = EntryImageForm, extra = 5)
	if request.method == 'POST':
		# Getting the submitted data
		entry_form = NewEntryForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES, queryset = EntryImage.objects.none())

		# Validitating that the two forms
		if entry_form.is_valid() and formset.is_valid():
			# Getting all data submitted and the user information
			numOfDescriptions = entry_form.cleaned_data['numOfDescriptions']
			username = request.session.get('username')
			author = User.objects.get(username = username)

			# Creating a new entry with given info
			newEntry = Entry(title = entry_form.cleaned_data['title'], author = author, numOfDescriptions = entry_form.cleaned_data['numOfDescriptions'])

			# Collecting all the images and descriptions submitted
			if entry_form.is_valid() and formset.is_valid():
				img_count = 0
				img_entries_list = []
				for img in formset.cleaned_data:
					if img:
						the_pic = img.get('image')
						the_desc = img.get('description')
						img_count = img_count + 1

						# Creating a new entry image object and appending it to list
						new_entry_img = EntryImage(entry = newEntry, image = the_pic, description = the_desc)
						img_entries_list.append(new_entry_img)

				# Double checking form validity
				if img_count != int(numOfDescriptions):
					message = "Error! Number of descriptions do not match the amount of images uploaded"
					new_form = NewEntryForm()
					ImageFormSet = ImageFormSet(queryset=EntryImage.objects.none())
					return render(request, 'newEntry.html', {'entryform':new_form, 'message':message, 'imageformset':ImageFormSet})
				else:
					# Success message for new entry
					message = "You Have Successfully Added A New Entry!"
					# Saving New Entry and All New Entry Images 
					newEntry.save()
					for img_entry in img_entries_list:
						img_entry.save()
					return redirect('homepage') # redirecting to homepage to show new entry
	else:
		# Original form for the initial new entry page display
		form = NewEntryForm()
		ImageFormSet = ImageFormSet(queryset=EntryImage.objects.none())
		return render(request, 'newEntry.html', {'entryform':form, 'imageformset':ImageFormSet})

# Credit to https://stackoverflow.com/questions/20177779/how-can-i-change-form-field-values-after-calling-the-is-valid-method/45050312
# Credit to https://stackoverflow.com/questions/18534307/change-a-form-value-before-validation-in-django-form
# Credit to https://medium.com/@qasimalbaqali/upload-multiple-images-to-a-post-in-django-ff10f66e8f7a
# Credit to https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
# Credit to https://docs.djangoproject.com/en/3.1/topics/http/sessions/