from django.shortcuts import render, redirect
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

#def listarProds(request):
#    productos=Productos.objects.all()  # Equivalente a decir SELECT * FROM PRODUCTOS
    # print(productos)
#    return render(request,"listarprods.html", {"misProductos": productos})

# form = ProductoFrm()
    # # return render(request,"crearprods.html", {'form': form})
    # context = {
    #     'form':form
    # }
    # return render(request,"crearprods.html", contexto)
    # else:
    #     form = ProductoFrm(request.POST)
    #     print(form)
    # return render(request,"crearprods.html", context)
