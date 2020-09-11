
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.website, name='index'),
    path('email',views.email,name='email'),
]
