from django import forms
from models import GENDER_CHOICES
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators

def userNameValidator(value):
    try:
        user = User.objects.get(username = value)
    except User.DoesNotExist:
        return True
    raise ValidationError('Email zaten var.')

class UserForm(forms.Form):
    firstName = forms.CharField(max_length = 30, widget=forms.TextInput(attrs={'title':"FirstName", 'placeholder': "First Name"}))
    lastName = forms.CharField(max_length = 30, widget=forms.TextInput(attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Email"}),
            validators = [userNameValidator])
    password = forms.CharField(label = "Create Password", widget = forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(label = "Confirm Your Password", widget = forms.PasswordInput(attrs={'placeholder': "Password"}))
    #birthdate = forms.DateField(widget = SelectDateWidget( years = range(1930, 2012)))
    #gender = forms.ChoiceField(choices = GENDER_CHOICES)
    #photo = forms.ImageField(required = False)

    def clean(self):
        super(forms.Form, self).clean()
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                self._errors['password'] = ["Parololar eslesmeli."]
                self._errors['Password2'] = ["Parololar eslesmeli."]
        return self.cleaned_data
class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'label':'','placeholder': 'username'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'label':'','placeholder': 'password'}))

