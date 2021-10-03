from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse

from Tienda.models import *
from Tienda.Forms import *

# Create your views here.

def Formulario(request):
    return render(request, "Formulario.html")

def TablaProductos(request):
    productos=Producto.objects.all()  # Equivalente a decir SELECT * FROM PRODUCTOS
    # print(productos)
    return render(request,"TablaProductos.html", {"misProductos": productos})

def CrearProductos(request):
    if request.method == 'GET':
        form = ProductoFrm()
    else:
        form = ProductoFrm(request.POST)
    contexto = {'Formulario':form}
    if form.is_valid():
        form.save()
        return redirect('TablaProductos')
    return render(request,'CrearProductos.html', contexto)

def vistaAccionFrm(request):
    if request.GET['Nombre']:  
    #mensaje = request.GET["Nombre"] + " NO se encuentra entre nuestos Productos"
        miVarName=request.GET["Nombre"]
        misprods=Producto.objects.filter(nombreProducto__icontains=miVarName) # WHERE nomProd Like '%miVarName%'
        return render(request,"Resultados.html", {"articulos":misprods, "query":miVarName})
    else:
        mensaje = "No hay información..."
    return HttpResponse(mensaje)

def editarProducto(request, idProducto):
    producto = Producto.objects.get( idProducto=idProducto )
    if request.method == 'GET':
        form = ProductoFrm(instance=producto)
    else:
        form = ProductoFrm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('TablaProductos')
    contexto = {
        'Formulario':form
        }
    return render (request, 'CrearProductos.html', contexto)

def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    #Ventana de confirmacion
    confirmar=True
    if confirmar:
        producto.delete()
    return redirect('TablaProductos')