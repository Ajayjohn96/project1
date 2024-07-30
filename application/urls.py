from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('index', views.welcome, name='home'),
    path('items', views.items, name= 'items'),
    path('about', views.about, name= 'about'),
]
