
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('contact', views.contact,name='contact'),
    path('menu', views.menu,name='menu'),
    
]

