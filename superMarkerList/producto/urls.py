from django.contrib import admin
from django.urls import path
from producto import views as vistasProducto

urlpatterns = [
    path('productos/', vistasProducto.inicio),
]
