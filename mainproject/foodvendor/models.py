from django.db import models


# Create your models here.
class Vendormodel(models.Model):
    vendorname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    itemquantity = models.IntegerField()

