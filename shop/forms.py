from django import forms
from django.contrib.auth.models import User
from shop.models import category,product

class Registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()  


class categoryform(forms.ModelForm):
    class Meta:
        model=category
        fields=['name']

class Addproduct(forms.ModelForm):
    class Meta:
        model=product    
        fields="__all__"
