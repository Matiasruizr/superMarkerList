from django import forms
from django.contrib.auth.models import User
from .models import Tienda

class SignUpFormT():
    nombre = forms.CharField(max_length=140, required=True)
    ubicacion = forms.CharField(max_length=140, required=True)
    ciudad = forms.CharField(max_length=140,required=True)
    aprobado  forms.BooleanField(default=True)
    region = forms.CharField(max_length=140,required=True)
    

    class Meta:
        model = Tienda
        fields = (
            'nombre',
            'ubicacion',
            'ciudad',         
            'aprobado',
            'region',           
        )
        