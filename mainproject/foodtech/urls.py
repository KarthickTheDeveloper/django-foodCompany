from django.urls import path
from . import views

urlpatterns = [
    path('tech/', views.tech),
    path('register-tech/', views.register),
    path('login-tech/', views.login)
]
