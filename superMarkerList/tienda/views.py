from django.shortcuts import render, redirect
from .models import Tienda
from .forms import SignUpFormT
from django.views.generic import CreateView,
# Create your views here.


class SignUpViewT(CreateView):
    model = Tienda
    form_class = SignUpFormT

    def form_valid(form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        return redirect('/')