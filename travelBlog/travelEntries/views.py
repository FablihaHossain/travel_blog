from django.shortcuts import render
from .models import User, Entry, EntryImage

def index(request):
	# Getting all users
	users = User.objects.all()

	# Getting all entries
	entries = Entry.objects.all()

	# Getting all entry images
	images = EntryImage.objects.all()

	return render(request, 'index.html', {'users':users, 'entries':entries, 'images':images})

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'registration.html')