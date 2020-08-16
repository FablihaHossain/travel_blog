from django.contrib import admin
from .models import User, Entry, EntryImage
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'username', 'email', 'role']

class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['title', 'author', 'descriptions']
admin.site.register(Entry, ArrayModelAdmin)

@admin.register(EntryImage)
class EntryImages(admin.ModelAdmin):
	list_display = ['entry', 'image']

# Credit to https://github.com/gradam/django-better-admin-arrayfield