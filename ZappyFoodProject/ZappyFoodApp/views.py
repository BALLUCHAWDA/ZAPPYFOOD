from django.shortcuts import render
from django.http import HttpResponseRedirect
from ZappyFoodApp.forms import UserForm,AddProduct,CustomerUpdate,Checkout,OrderForm
from django.contrib.auth.decorators import login_required
from ZappyFoodApp.models import AddProduct,User,Order
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import  Paginator
from django.core.mail import send_mail
from django.conf import settings

#HOMEVIEW
def homeView(request):
	return render(request,"zappyapp/home.html" )

def home(request):
    return render(request,"zappyapp/home.html")

#ABOUTUS
def about(request):
    return render(request,"zappyapp/about.html")

#ALLPRODUCT VIEW
def allview(request):
    blist0 = AddProduct.objects.all().filter(productCategory='0' )
    blist1 = AddProduct.objects.all().filter(productCategory='1' )
    blist2 = AddProduct.objects.all().filter(productCategory='2' )
    mydict = {"blist0":blist0,"blist1":blist1,"blist2":blist2}
    return render(request,"zappyapp/allproduct.html",context=mydict)

#SIGNUPVIEW
def signupview(request):
    if request.method=='GET':
        sform=UserForm()
        return render(request,"zappyapp/signup.html",{'sform':sform})
    if request.method=='POST':
        sform = UserForm(request.POST)
        if sform.is_valid():
            user=sform.save()
            user.set_password(user.password)
            user.save()
            #return HttpResponseRedirect(reverse('login'))
            return render(request,'zappyapp/success.html',{'msg':"RAGISTRATION SUCCESS...."})

#VIEWCART
def viewCart(request):
    products=AddProduct.objects.all()
    productPrice,productPics, productName = [], [], []
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            productPics.append(AddProduct.objects.get(id=i).productPics.url)
            productName.append(AddProduct.objects.get(id=i).productName)
            productPrice.append(AddProduct.objects.get(id=i).productPrice*int(j))
    total=sum(productPrice)
    dict={'productPrice':productPrice,'total':total,'productPics':productPics,'productName':productName}
    print(productName)
    if not request.COOKIES.items():
        productPrice, productPics, productName, total = [], [], [], 0
    return render(request,"zappyapp/cart.html",context=dict)

#CART
def cart(request):
    response=render(request,"zappyapp/home.html" )
    id=request.GET.get("id")
    print(id)
    item=request.GET.get('items')
    if id in request.COOKIES.keys():
        items=int(request.COOKIES.get(id))
        item=int(item)+items
        response.set_cookie(id,item)
    else:
        response.set_cookie(id,item)
    return response
	
#CART_HOME
def cart_home(request):
    length=0
    for k,v in request.COOKIES.items():
        if k.isdigit() and v.isdigit():
            length+=1
    response=render(request,"zappyapp/cart.html")
    response.set_cookie('length',length)
    return response

@login_required
def profile(request):
    return render(request, 'zappyapp/profile.html')

@login_required
def customer(request):
    if request.method == 'POST':
        customer_form = CustomerUpdate(request.POST,request.FILES,instance=request.user.Customer)
        if customer_form.is_valid():
            customer_form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        customer_form = CustomerUpdate(request.POST,request.FILES,instance=request.user.Customer)
    return render(request, 'zappyapp/customer.html',{'customer_form':customer_form})

#CARTDELETE
def cartdelelete(request):
    response=render(request,"zappyapp/home.html" )
    id=request.GET.get('id')
    print(id)
    if id in request.COOKIES.keys():
        response.delete_cookie(id)
    return response

@login_required
def checkout(request):
    products=[]
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            products.append(AddProduct.objects.get(id=i).productName)
    if request.method == 'POST':
        response=render(request,'zappyapp/success.html')
        ch_form = Checkout(request.POST)
        if ch_form.is_valid():
            ch_form.save()
            for id in request.COOKIES.items():
                if id.isdigit() or id=='length':
                    print(id)
                    response.delete_cookie(id)
            return response
    else:
        ch_form = Checkout()
    return render(request, 'zappyapp/checkout.html',{'ch_form':ch_form})

#CHECKOUTSUCCESS
def checkoutsuccess(request):
    return render(request, 'zappyapp/checkoutsuccess.html')

@login_required
def orderhistory(request):
    order=Order.objects.filter(id=request.user.id).order_by('-id')
    return render(request, 'zappyapp/orderhistory.html',{'order':order})
