from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name
        

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(default= '', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    CAT = (
        ('In Door', 'In Door'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(choices = CAT, max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    price= models.FloatField()
    tags = models.ManyToManyField(Tag)



    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'), 
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices = STATUS, max_length=255, null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    note = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.product.name


