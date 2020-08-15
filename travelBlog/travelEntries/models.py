from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
	ROLES = [('G', 'General User'), ('A', 'Admin User')]
	name = models.CharField(max_length=100, blank = False)
	username = models.CharField(max_length=100, blank = False)
	email = models.EmailField(blank = False)
	password = models.CharField(max_length = 300, blank = False)
	role = models.CharField(max_length = 20, choices = ROLES, blank = False)
	# Users can have multiple entries in the blog site
	#entries = models.ManyToManyField('Entry', blank = True)

	# Print statement for Python Shell
	def __str__(self):
		return self.name

class Entry(models.Model):
	title = models.CharField(max_length = 400, blank = False)
	author = models.ForeignKey('User', on_delete=models.CASCADE)
	#descriptions = ArrayField(models.charField(max_length = 500), size = 5)
	#images = ArrayField(models.ImageField(upload_to(user_entry_pathname)), size = 5)

	# Print statement for Python Shell	
	def __str__(self):
		return self.title

def user_entry_pathname(instance, filename):
	return 'user{0}/{1}'.format(instance.user.id, filename)
# Credit to https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/#arrayfield