from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vendormodel


# Create your views here.
def vendor(request):
    return render(request, 'vendor/vendor.html')


def register(request):
    if request.method == 'POST':
        vendorname = request.POST["vendor-name"]
        email = request.POST["email"]
        password = request.POST.get("password1")
        repeatpassword = request.POST["password2"]
        itemname = request.POST.get("item-name")
        itemquantity = request.POST["item-quantity"]
        print(vendorname)
        print(email)
        print(password)
        print(repeatpassword)
        print(itemname)
        print(itemquantity)
        if password == repeatpassword:
            ven = Vendormodel(vendorname=vendorname,email=email,password=password,itemname=itemname,itemquantity=itemquantity).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/vendor/')
        else:
            messages.error(request, 'Passwords should be same!!!')
            return redirect('/login/')
    return render(request, 'vendor/rl/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password1"]
        print(email)
        print(password)
        try:
            ven = Vendormodel.objects.get(email=email)
            messages.success(request, "Login Success")
            return redirect('/vendor/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login/')
    return render(request, 'vendor/rl/index.html')
