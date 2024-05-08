from django import forms
from django.contrib.auth.models import User


class Registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()          

