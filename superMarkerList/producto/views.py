from django.shortcuts import render
from .forms import formProduct
from .models import Producto
from django.views.generic import CreateView  

# Create your views here.
def inicio(request):
    return render(request,  'productos/inicio.html', {})

class SignUpViewP(CreateView):
    model = Producto
    form_class = formProduct
   
    # return render(request, 'productos/new.html', {'form': form})


