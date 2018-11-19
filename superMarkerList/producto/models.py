# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    # id_producto = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    aprobado =  models.BooleanField
    region = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
    )
    estado = models.CharField(max_length=10, choices=estado)