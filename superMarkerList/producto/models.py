# Create your models here.
from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.


class Product(models.Model):
    # id_producto = models.CharField(max_length=200)
    nombre_producto = models.CharField(max_length=200)
    costo_presupuestado = models.IntegerField(default=0)
    costo_real = models.IntegerField(default=0)
    id_tienda = models.CharField(max_length=200)
    comentarios = models.CharField(max_length=200)
    unidad =  models.IntegerField(default=0)
    aprobado =  forms.BooleanField
    descripcion = models.CharField(max_length=200)