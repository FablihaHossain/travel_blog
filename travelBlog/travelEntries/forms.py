from django import forms
from .models import User

class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=100)
	password = forms.CharField(label="password", max_length=300, widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'username', 'password', 'role']
		widgets = {'password':forms.PasswordInput, 'role':forms.HiddenInput}
		#role = forms.CharField(widget=forms.HiddenInput())

# extra notes
# example = ChoiceField(label="Example", choices = [('1'), ('2')....])
# widget = forms.Textarea
# image = forms.ImageField() => add request.FILES alongside request.POST in views.py

# Note to self: Perhaps add another field into Entry model that keeps track of how many descriptions there will be