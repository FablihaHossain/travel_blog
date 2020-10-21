from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

# User Model 
class User(models.Model):
	ROLES = [('G', 'General User'), ('A', 'Admin User')] # Currently only two roles
	name = models.CharField(max_length=100, blank = False)
	username = models.CharField(max_length=100, blank = False)
	email = models.EmailField(blank = False)
	password = models.CharField(max_length = 300, blank = False)
	role = models.CharField(max_length = 20, choices = ROLES, blank = False)

	# Print statement for Python Shell and Admin Functionality
	def __str__(self):
		return self.username

# Entry Model
class Entry(models.Model):
	title = models.CharField(max_length = 400, blank = False)
	# Each entry belongs to one user in the database
	author = models.ForeignKey('User', on_delete=models.CASCADE)
	numOfDescriptions = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	# descriptions = ArrayField(models.CharField(max_length = 500), size = 5)

	# Print statement for Python Shell and Admin Functionality
	def __str__(self):
		return self.title

# Sub model that allows for uploads of image files
class EntryImage(models.Model):
	# Each image uploaded must pertain to a particular entry in the database
	entry = models.ForeignKey('Entry', on_delete=models.CASCADE)

	# Each image should have a corresponding description
	description = models.CharField(max_length = 500, default = "No Description Given")

	# Defines pathname for uploaded images, each entry will have their own directory
	def get_upload_path(instance, filename):
		return 'entryImages/entry_{0}/{1}'.format(instance.entry.id, filename)

	# Image source
	image = models.ImageField(upload_to = get_upload_path)

# Credit to https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/#arrayfield
# Credit to https://github.com/gradam/django-better-admin-arrayfield
# Credit to https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.FileField.upload_to
# Credit to https://www.reddit.com/r/django/comments/2q5u0p/way_to_make_a_min_and_max_values_restriction_on_a/