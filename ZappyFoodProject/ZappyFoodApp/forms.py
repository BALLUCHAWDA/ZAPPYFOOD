

from django import forms
from django.contrib.auth.models import User
from ZappyFoodApp.models import AddProduct,Customer,Order

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')

class AddProductForm(forms.ModelForm):
    class Meta:
        model=AddProduct
        fields=('productCategory','productName','productPrice','productPics','productDescription','quantity')
        widgets={

    #FOOD=(('re','ready to eat'),('rc','ready to Cook'))
        'category':forms.Select(attrs={'class':'select'},choices=(('0','Ready To Eat'),('1','Ready To Drink'),('2','Ready To Cook'),)),
        'description':forms.Textarea(attrs={'placeholder':'Enter Post Description'}),
        }
class CustomerUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['images','customer_address','mobile',]
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['pid','delievery_address','status']
class Checkout(forms.ModelForm):
    delievery_address=forms.CharField(required=True)
    class Meta:
        model=Order
        widgets = {'delievery_address': forms.TextInput(attrs={'placeholder': 'Same as Billing Address'})}
        fields=['delievery_address']
