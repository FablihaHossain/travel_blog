from django import forms
from .models import User

class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=100)
	password = forms.CharField(label="password", max_length=300, widget=forms.PasswordInput)
	
class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'username', 'password']
		widgets = {'password':forms.PasswordInput}
	# name = forms.CharField(label="name", max_length=100)
	# email = forms.EmailField(label="email")
	# username = forms.CharField(label="username", max_length=100)
	# password = forms.CharField(label="password", max_length=300)

# extra notes
# example = ChoiceField(label="Example", choices = [('1'), ('2')....])
# widget = forms.Textarea
# image = forms.ImageField() => add request.FILES alongside request.POST in views.py

# Note to self: Perhaps add another field into Entry model that keeps track of how many descriptions there will be