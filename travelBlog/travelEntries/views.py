from django.shortcuts import render
from .models import User, Entry, EntryImage
from django.http import Http404
from .forms import LoginForm, RegistrationForm, NewEntryForm

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
			register_form.save()
			# creating new form 
			new_Form = RegistrationForm()
			return render(request, 'registration.html', {'registrationform':new_Form, 'message':message})
	else:
		register_form = RegistrationForm()
		return render(request, 'registration.html', {'registrationform':register_form})

def newEntry(request):
	if request.method == 'POST':
		entry_form = NewEntryForm(request.POST)
		if entry_form.is_valid():
			message = 'You entered %s and %s' % (entry_form.cleaned_data['title'], entry_form.cleaned_data['descriptions'])
			new_form = NewEntryForm()
			return render(request, 'newEntry.html', {'entryform':new_form, 'message':message})
	else:
		form = NewEntryForm()
		return render(request, 'newEntry.html', {'entryform':form})

def viewEntry(request, entry_id):
	try:
		entry = Entry.objects.get(id = entry_id)
		images = EntryImage.objects.all()
	except Entry.DoesNotExist:
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'viewEntry.html', {'entry':entry,'images':images})

# Credit to https://stackoverflow.com/questions/20177779/how-can-i-change-form-field-values-after-calling-the-is-valid-method/45050312
# Credit to https://stackoverflow.com/questions/18534307/change-a-form-value-before-validation-in-django-form