from django.urls import path
from . import views

urlpatterns = [
    path('vendor/', views.vendor),
    path('register/', views.register),
    path('login/', views.login),
]
