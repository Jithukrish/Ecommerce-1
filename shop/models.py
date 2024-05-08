from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.name
    
class product(models.Model): 
    name=models.CharField(max_length=30)  
    description=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    colour=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    image=models.ImageField(upload_to="images",null=True)
    category=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class cart(models.Model):
    item=models.ForeignKey(product,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    quantity=models.PositiveIntegerField()
    options=(
        ("added","added"),("purchased","purchased"),("removed","removed")
    )
    status=models.CharField(max_length=20,choices=options,default="added")





