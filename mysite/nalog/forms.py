from django import forms
from django.contrib.auth.models import User
from .models import UserResults, UserProfile

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            #field.widget.attrs['placeholder'] = 'Enter the ' + field_name                         

class UserForm(BaseForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(BaseForm):
    class Meta:
        model = UserProfile
        fields = ()

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100, widget=forms.TextInput(attrs = {'class': 'form-control'}))
	sender = forms.EmailField(widget=forms.EmailInput(attrs = {'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control'}))
	copy = forms.BooleanField(required = False)