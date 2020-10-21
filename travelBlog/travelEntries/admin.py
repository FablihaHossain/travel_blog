from django.contrib import admin
from .models import User, Entry, EntryImage
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# User Details
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'username', 'email', 'role']

# Details for Entry Images
class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['title', 'author',]
admin.site.register(Entry, ArrayModelAdmin)

# Entry Details
@admin.register(EntryImage)
class EntryImages(admin.ModelAdmin):
	list_display = ['entry', 'image', 'description']

# Credit to https://github.com/gradam/django-better-admin-arrayfield