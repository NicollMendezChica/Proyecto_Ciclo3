from django.shortcuts import render, redirect
from django.http import HttpResponse

from Tienda.models import *
from Tienda.Forms import *

# Create your views here.

def formulario(request):
    return render(request, "Formulario.html")

def TablaProductos(request):
    productos=Producto.objects.all()  # Equivalente a decir SELECT * FROM PRODUCTOS
    # print(productos)
    return render(request,"TablaProductos.html", {"misProductos": productos})

def crearProds(request):
    if request.method == 'GET':
        form = ProductoFrm()
    else:
        form = ProductoFrm(request.POST)

    contexto = {'Formulario':form}
    
    if form.is_valid():
        form.save()
        return redirect('ListadoTabla')

    return render(request,'CrearProductos.html', contexto)
