from django.urls import path
from customer import views

urlpatterns=[
    path("log/",views.loginview.as_view(),name="log"),
    path("reg/",views.Sign.as_view(),name="reg"),

]