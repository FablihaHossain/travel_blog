from django.shortcuts import render
from .models import User, Entry, EntryImage
from django.http import Http404
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

	return render(request, 'index.html', {'users':users, 'entries':entries, 'images':images})

# Login Page
def login(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			message = 'You entered %s and %s' % (login_form.cleaned_data['username'], login_form.cleaned_data['password'])
			new_form = LoginForm()
			return render(request, 'login.html', {'loginform':new_form, 'message':message})
	else:
		form = LoginForm()
		return render(request, 'login.html', {'loginform':form})

# Registration Page
def register(request):
	if request.method == 'POST':
		# getting all the current registration information
		updated_request = request.POST.copy()
		# updating the role of the user 
		updated_request.update({'role': 'G'})
		# putting all updated information into the role
		register_form = RegistrationForm(updated_request)
		#register_form = RegistrationForm(request.POST)

		#role = request.POST['role']
		# checking if registration form is valid
		if register_form.is_valid():
			#register_form.cleaned_data['role'] = 'General User'
			message = 'You Entered name: %s, email: %s, username: %s, password: %s, role:%s' % (register_form.cleaned_data['name'],
				register_form.cleaned_data['email'],
				register_form.cleaned_data['username'],
				register_form.cleaned_data['password'],
				register_form.cleaned_data['role'])

			#new_user = register_form.save(commit=False)
			#print(new_user.role)
			#new_user.role = 'G'
			#print(new_user.role)
			#new_user.save()
			# saving new user
			# register_form.save()
			# creating new form 
			new_Form = RegistrationForm()
			return render(request, 'registration.html', {'registrationform':new_Form, 'message':message})
	else:
		register_form = RegistrationForm()
		return render(request, 'registration.html', {'registrationform':register_form})

# The homepage will contain all entries
def homepage(request):
	# Getting all entries
	entries = Entry.objects.all()

	# Getting all entry images
	images = EntryImage.objects.all()

	# Getting all authors
	authors = User.objects.all()

	listOfAuthorNames = []
	for entry in entries:
		for auth in authors:
			if entry.author == auth:
				listOfAuthorNames.append(auth.name)

	return render(request, 'homepage.html', {'entries':entries, 'images':images, 'data': zip(entries, listOfAuthorNames)})

# Viewing Entries Individually Based on Entry ID
def viewEntry(request, entry_id):
	try:
		entry = Entry.objects.get(id = entry_id)
		images = EntryImage.objects.all()

		currentImages = []
		for img in images:
			if img.entry_id == entry.id:
				currentImages.append(img)
	except Entry.DoesNotExist:
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'viewEntry.html', {'entry':entry,'images':currentImages})









# NEEDS FIXING WITH THE NEW CHANGE
def newEntry(request):
	# ImageFormSet = modelformset_factory(EntryImage,fields = ('image',))
	ImageFormSet = modelformset_factory(EntryImage, form = EntryImageForm, extra = 5)
	if request.method == 'POST':
		entry_form = NewEntryForm(request.POST)
		# entry_image_form = EntryImageForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES, queryset = EntryImage.objects.none())
		#if entry_form.is_valid() and entry_image_form.is_valid():
		if entry_form.is_valid() and formset.is_valid():
			# message = 'You entered %s and %s and %s' % (entry_form.cleaned_data['title'], 
			# 	entry_form.cleaned_data['descriptions'],
			# 	entry_form.cleaned_data['author'])

			message = "You Have Successfully Added A New Entry!"
			print(len(formset.cleaned_data))

			# saving all the infos
			numOfDescriptions = entry_form.cleaned_data['numOfDescriptions']
			author = User.objects.get(username = entry_form.cleaned_data['author'])
			newEntry = Entry(title = entry_form.cleaned_data['title'], author = author, numOfDescriptions = entry_form.cleaned_data['numOfDescriptions'])
			# , descriptions = entry_form.cleaned_data['descriptions']
			# newEntry.save()
			# imgformset = formset.save(commit=False)
			img_count = 0
			for img in formset.cleaned_data:
				if img:
					the_pic = img.get('image')
					the_desc = img.get('description')
					img_count = img_count + 1

					print(the_pic)
					print(the_desc)
					print("")
					# new_img = EntryImage(entry = newEntry, image = the_pic)
					# new_img.save()
					# print(img.get('image'))

			if img_count != numOfDescriptions:
				message = "Error! Number of descriptions do not match the amount of images uploaded"
			new_form = NewEntryForm()
			ImageFormSet = ImageFormSet(queryset=EntryImage.objects.none())
			# new_form2 = EntryImageForm()
			return render(request, 'newEntry.html', {'entryform':new_form, 'message':message, 'imageformset':ImageFormSet})
	else:
		form = NewEntryForm()
		ImageFormSet = ImageFormSet(queryset=EntryImage.objects.none())
		# second_form = EntryImageForm()
		return render(request, 'newEntry.html', {'entryform':form, 'imageformset':ImageFormSet})



def editEntry(request, entry_id):
	try:
		entry_image_form = EntryImageForm()
		entry = Entry.objects.get(id = entry_id)
		if request.method == 'POST':
			entry_image_form = EntryImageForm(request.POST)
			if entry_image_form.is_valid():
				print('form is valid')
			else:
				print('form is not valid')
	except Entry.DoesNotExist:
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'editEntry.html', {'entry':entry, 'imageform':entry_image_form})


# def editEntry(request, entry_id):
# 	try:
# 		entry = Entry.objects.get(id = entry_id)
# 		images = EntryImage.objects.all()
# 		entry_image_form = 'test form'
		# print('before new form')
		# entry_image_form = EntryImageForm()
		# print('new form created')
		# if request.method == 'POST':
		# 	entry_image_form = EntryImageForm(request.POST)
		# 	if entry_image_form.is_valid():
		# 		print('form is valid')
		# 	else:
		# 		print('form is not valid')
	# except Entry.DoesNotExist:
	# 	raise Http404(f'Entry with id {entry_id} does not exist')
	# return render(request, 'editEntry.html', {'entry':entry, 'images':images, 'imageform':entry_image_form})

	# if request.method == 'POST':
	# 	entry_image_form = EntryImageForm(request.POST)
	# 	if entry_image_form.is_valid():
	# 		message = 'You entered %s and image %s' % (entry_image_form.cleaned_data['entry'],
	# 			entry_image_form.cleaned_data['image'])
	# 		new_form2 = EntryImageForm()
	# 		return render(request, 'editEntry.html', {'message':message, 'imageform':new_form2})
	# 	else:
	# 		form = EntryImageForm()
	# 		return render(request, 'editEntry.html', {'imageform':form})

# Credit to https://stackoverflow.com/questions/20177779/how-can-i-change-form-field-values-after-calling-the-is-valid-method/45050312
# Credit to https://stackoverflow.com/questions/18534307/change-a-form-value-before-validation-in-django-form
# Credit to https://medium.com/@qasimalbaqali/upload-multiple-images-to-a-post-in-django-ff10f66e8f7a
# Credit to https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django