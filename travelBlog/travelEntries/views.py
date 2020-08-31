from django.shortcuts import render
from .models import User, Entry, EntryImage
from django.http import Http404
from .forms import LoginForm, RegistrationForm

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
		register_form = RegistrationForm(request.POST)
		if register_form.is_valid():
			message = 'You Entered name: %s, email: %s, username: %s, password: %s' % (register_form.cleaned_data['name'],
				register_form.cleaned_data['email'],
				register_form.cleaned_data['username'],
				register_form.cleaned_data['password'])
			new_Form = RegistrationForm()
			return render(request, 'registration.html', {'registrationform':new_Form, 'message':message})
	else:
		register_form = RegistrationForm()
		return render(request, 'registration.html', {'registrationform':register_form})

def newEntry(request):
	return render(request, 'newEntry.html')

def viewEntry(request, entry_id):
	try:
		entry = Entry.objects.get(id = entry_id)
		images = EntryImage.objects.all()
	except Entry.DoesNotExist:
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'viewEntry.html', {'entry':entry,'images':images})