from django import forms
from django.contrib.auth.models import User

from .models import Sample

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ['sample_logo', 'sample_title']