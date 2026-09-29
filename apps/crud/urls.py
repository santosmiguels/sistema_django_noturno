# from django import path - errei aqui!
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]