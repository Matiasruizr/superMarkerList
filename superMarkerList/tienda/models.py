# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.


class Tienda(models.Model):
    # id_tienda = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    aprobado = models.BooleanField(default=True)
    region = (
        ('Region de Arica y Parinacota', 'Arica'),
        ('Region de Tarapaca', 'Iquique'),
        ('Region de Antofagasta', 'Antofagasta'),
        ('Region de Atacama', 'Copiapo'),
        ('Region de Coquimbo ', 'La Serena'),
        ('Region de Valparaiso', 'Valparaiso'),
        ('Region Metropolitana de Santiago', 'Santiago'),
        ('Region del Libertador General Bernardo OHiggins', 'Rancagua'),
        ('Region del Maule', 'Talca'),
        ('Region de Ñuble', 'Chillan'),
        ('Region del Biobio', 'Concepcion'),
        ('Region de la Araucania', 'Temuco'),
        ('Region de Los Rios', 'Valdivia'),
        ('Region de Los Lagos', 'Puerto Montt'),
        ('Region de Aysen', 'Coyhaique'),
        ('Region de Magallanes y de la Antartica Chilena', 'Punta Arenas'),
    )
    region = models.CharField(max_length=200)
  