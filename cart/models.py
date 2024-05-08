from django.db import models
from django.contrib.auth.models import User
from shop.models import product

# Create your models here.
class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(product,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    address=models.TextField()
    contact=models.CharField(max_length=30)

    def __str__(self):
        return self.user

class Basket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    options=(
        ("added","added"),("purchased","purchased"),("removed","removed")
    )
    status=models.CharField(max_length=20,choices=options,default="added")
    price=models.PositiveIntegerField()


