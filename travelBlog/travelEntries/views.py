from django.shortcuts import render
from .models import User, Entry, EntryImage
from django.http import Http404

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
	return render(request, 'login.html')

# Registration Page
def register(request):
	return render(request, 'registration.html')

def newEntry(request):
	return render(request, 'newEntry.html')

def viewEntry(request, entry_id):
	try:
		entry = Entry.objects.get(id = entry_id)
		images = EntryImage.objects.all()
	except Entry.DoesNotExist:
		raise Http404(f'Entry with id {entry_id} does not exist')
	return render(request, 'viewEntry.html', {'entry':entry,'images':images})