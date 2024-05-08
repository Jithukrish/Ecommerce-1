from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView
from shop.forms import Registerform,Loginform,categoryform,Addproduct
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from shop.models import category,product
from django.urls import reverse_lazy

# Create your views here.

# class Home(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"home.html")
class Home(TemplateView):
    template_name="home.html"


class Sign(FormView):
    template_name="reg.html"
    form_class=Registerform
    # def get(self,request,*args,**kwargs):
    #     form=Registerform()
    #     return render(request,"reg.html",{"form":form})
    

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
    template_name="login.html"
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
            return redirect("login")    

    # def get(self,request,*args,**kwargs):
    #     form=Loginform()
    #     return render(request,"login.html",{"form":form})
        
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
            

class addcategory(CreateView,ListView):
    template_name="category.html"
    form_class=categoryform
    model=category
    success_url=reverse_lazy("category")
    context_object_name="data"

class removecategory(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        category.objects.get(id=id).delete()
        return redirect("category")

class Addproduct(CreateView,ListView):
    template_name="product.html"
    form_class=Addproduct
    model=product
    success_url=reverse_lazy("add")
    context_object_name="qs"

class delproduct(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product.objects.get(id=id).delete()
        return redirect("add")



