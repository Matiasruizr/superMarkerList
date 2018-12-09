from django.shortcuts import render
from .forms import formProduct
# Create your views here.
def inicio(request):
    return render(request,  'productos/inicio.html', {})

def new(request):
    form = formProduct
   
    return render(request, 'productos/new.html', {'form': form})


