from django.urls import path
from shop import views
urlpatterns=[
    path("home/",views.Home.as_view(),name="home"),
    path("login/",views.loginview.as_view(),name="login"),
    path("create/",views.addcategory.as_view(),name="category"),
    path("remove/<int:pk>",views.removecategory.as_view(),name="del"),
    path("add/",views.Addproduct.as_view(),name="add"),
    path("del/<int:pk>/",views.delproduct.as_view(),name="delete"),

]