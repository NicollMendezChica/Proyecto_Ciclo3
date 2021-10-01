from django.shortcuts import render
from Tienda.models import *

# Create your views here.

def formulario(request):
    return render(request, "Formulario.html")

def TablaProductos(request):
    productos=Producto.objects.all()  # Equivalente a decir SELECT * FROM PRODUCTOS
    # print(productos)
    return render(request,"TablaProductos.html", {"misProductos": productos})