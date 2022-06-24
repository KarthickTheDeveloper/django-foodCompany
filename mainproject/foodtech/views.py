from django.shortcuts import render, redirect
from .models import Techmodel
from django.contrib import messages


# Create your views here.
def tech(request):
    return render(request, 'tech/tech.html')


def register(request):
    if request.method == 'POST':
        username = request.POST["user-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        repeatpassword = request.POST["password2"]
        phone = request.POST["mobile"]
        if password == repeatpassword:
            te = Techmodel(name=username,mail=email,password=password,phone=phone).save()
            messages.info(request, 'Successfully Registered')
            return redirect('/login-tech/')
        else:
            messages.error(request, 'Passwords should be same!!!')
    return render(request, 'tech/rl/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password1"]
        # print(email)
        # print(password)
        try:
            te = Techmodel.objects.get(mail=email)
            messages.success(request, "Login Success")
            return redirect('/tech/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login-tech/')
    return render(request, 'tech/rl/index.html')


