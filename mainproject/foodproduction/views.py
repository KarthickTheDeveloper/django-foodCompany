from django.shortcuts import render, redirect
from .models import Productionmodel
from django.contrib import messages


# Create your views here.
def production(request):
    return render(request, 'production/production.html')


def register(request):
    if request.method == 'POST':
        username = request.POST["user-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        repeatpassword = request.POST["password2"]
        phone = request.POST["mobile"]
        if password == repeatpassword:
            pr = Productionmodel(name=username,mail=email,password=password,phone=phone).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/login-production/')
        else:
            messages.error(request, 'Passwords should be same!!!')
    return render(request, 'production/rl/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password1"]
        # print(email)
        # print(password)
        try:
            pr = Productionmodel.objects.get(mail=email)
            messages.success(request, "Login Success")
            return redirect('/production/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login-production/')
    return render(request, 'production/rl/index.html')


