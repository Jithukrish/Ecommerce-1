from django.shortcuts import render,redirect
from django.views.generic import View,FormView
from shop.forms import Registerform,Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.

class Sign(FormView):
    template_name="regg.html"
    form_class=Registerform
    
    

    def post(self,request,*args,**kwargs):
        form=Registerform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            User.objects.create_user(**form.cleaned_data)
            print("success")
        else:
            print("get out")
        return redirect("home")
    
class loginview(FormView):
    template_name="loggin.html"
    form_class=Loginform

    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print("success")
                return redirect("home")
            else:
                print("error")
            return redirect("log")        
