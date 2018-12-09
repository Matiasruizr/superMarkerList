from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=140, required=True)
    apellido = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombre',
           
            'apellido',
            'password1',
            'password2', 
         
            
        )
        