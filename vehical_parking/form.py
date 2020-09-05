from django.contrib.auth.models import User
from .models import vehical
from django.contrib.auth.forms import AuthenticationForm
from django import forms
class userlogin(AuthenticationForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}) ,required=True)
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User