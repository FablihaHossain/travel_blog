from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField

class User(models.Model):
	ROLES = [('G', 'General User'), ('A', 'Admin User')]
	name = models.CharField(max_length=100, blank = False)
	username = models.CharField(max_length=100, blank = False)
	email = models.EmailField(blank = False)
	password = models.CharField(max_length = 300, blank = False)
	role = models.CharField(max_length = 20, choices = ROLES, blank = False)

	# Print statement for Python Shell
	def __str__(self):
		return self.username

class Entry(models.Model):
	title = models.CharField(max_length = 400, blank = False)
	author = models.ForeignKey('User', on_delete=models.CASCADE)
	descriptions = ArrayField(models.CharField(max_length = 500), size = 5)

	# Print statement for Python Shell	
	def __str__(self):
		return self.title

class EntryImage(models.Model):
	entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
	# Attempting to create a new path file for each entry
	pathname = 'entryImages/%s' % (entry)
	image = models.ImageField(upload_to = pathname)

	# Print statement for Python Shell	
	def __str__(self):
		return self.entry

# Credit to https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/#arrayfield
# Credit to https://github.com/gradam/django-better-admin-arrayfield