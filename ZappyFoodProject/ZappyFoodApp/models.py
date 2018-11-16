from django.db import models
from django.urls import reverse
from datetime import datetime
from PIL import Image

class User(models.Model):
    emailid=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30,null="True")

class AddProduct(models.Model):
    productCategory=models.CharField(max_length=50,null=True)
    productName=models.CharField(max_length=50)
    productPrice=models.IntegerField()
    productDescription=models.TextField(null="True")
    productPics=models.FileField(upload_to="documents/",null="True")
    quantity=models.PositiveIntegerField(null="True")

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (1024, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("products:id",kwrgs={'id':self.id})

class Customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE,null="True")
    customer_address=models.CharField(max_length=400,null="True")
    mobile = models.CharField(max_length=20,null="True")
    images = models.ImageField(upload_to='Customers',null="True")

    def __str__(self):
        return self.customer
class Order(models.Model):
    pid=models.ForeignKey(AddProduct,on_delete=models.CASCADE,null="True")
    delievery_address=models.CharField(max_length=200,null="True")
    status=models.IntegerField(null="True")
