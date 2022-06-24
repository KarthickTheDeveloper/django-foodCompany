from django.urls import path
from . import views

urlpatterns = [
    path('purchase/', views.purchase),
    path('login-purchase/', views.login),
    path('register-purchase/', views.register),
]
