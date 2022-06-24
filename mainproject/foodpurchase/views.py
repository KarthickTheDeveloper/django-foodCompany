from django.shortcuts import render, redirect
from .models import Purchasemodel
from django.contrib import messages


# Create your views here.
def purchase(request):
    return render(request, 'purchase/purchase.html')


def register(request):
    if request.method == 'POST':
        username = request.POST["user-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        repeatpassword = request.POST["password2"]
        phone = request.POST["mobile"]
        print(username)
        print(email)
        print(password)
        print(repeatpassword)
        print(phone)
        if password == repeatpassword:
            pur = Purchasemodel(name=username,mail=email,password=password,phone=phone).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/login-purchase/')
        else:
            messages.error(request, 'Passwords should be same!!!')
            return redirect('/register-purchase/')
    return render(request, 'purchase/rl/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password1"]
        # print(email)
        # print(password)
        try:
            pur = Purchasemodel.objects.get(mail=email)
            messages.success(request, "Login Success")
            return redirect('/purchase/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login-purchase/')
    return render(request, 'purchase/rl/index.html')



