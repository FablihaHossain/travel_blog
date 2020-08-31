from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=100)
	password = forms.CharField(label="password", max_length=300)

class RegistrationForm(forms.Form):
	name = forms.CharField(label="name", max_length=100)
	email = forms.EmailField(label="email")
	username = forms.CharField(label="username", max_length=100)
	password = forms.CharField(label="password", max_length=300)

# example = ChoiceField(label="Example", choices = [('1'), ('2')....])