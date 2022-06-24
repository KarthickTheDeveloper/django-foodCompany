from django.urls import path
from . import views

urlpatterns = [
    path('production/', views.production),
    path('register-production/', views.register),
    path('login-production/', views.login)
]
