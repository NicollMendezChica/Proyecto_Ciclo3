from django.shortcuts import render, redirect,  resolve_url
from django.http import HttpResponse

from Tienda.models import *
from Tienda.Forms import *

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

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

def FormularioUsuario(request):
    return render(request, "FormularioUsuario.html")

def TablaUsuario(request):
    usuario=Usuario.objects.only('idUsuario', 'nombre', 'idTienda')  # Equivalente a decir SELECT * FROM PRODUCTOS
    # print(productos)
    return render(request,"TablaUsuario.html", {"misUsuarios": usuario})

def CrearUsuario(request):
    if request.method == 'GET':
        form = UsuarioFrm()
    else:
        form = UsuarioFrm(request.POST)
    contexto = {'FormularioUsuario':form}
    if form.is_valid():
        form.save()
        return redirect('TablaUsuario')
    return render(request,'CrearUsuario.html', contexto)

def vistaAccionFrmUsuario(request):
    if request.GET['Nombre']:  
    #mensaje = request.GET["Nombre"] + " NO se encuentra entre nuestos Productos"
        miVarName=request.GET["Nombre"]
        misusers=Usuario.objects.filter(nombre__icontains=miVarName) # WHERE nomProd Like '%miVarName%'
        return render(request,"ResultadosUsuarios.html", {"usuarios":misusers, "query":miVarName})
    else:
        mensaje = "No hay información..."
    return HttpResponse(mensaje)

def editarUsuario(request, idUsuario):
    usuario = Usuario.objects.get( idUsuario=idUsuario )
    if request.method == 'GET':
        form = UsuarioFrm(instance=usuario)
    else:
        form = UsuarioFrm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('TablaUsuario')
    contexto = {
        'FormularioUsuario':form
        }
    return render (request, 'CrearUsuario.html', contexto)

def eliminarUsuario(request, idUsuario):
    usuario = Usuario.objects.get(idUsuario=idUsuario)
    #Ventana de confirmacion
    confirmar=True
    if confirmar:
        usuario.delete()
    return redirect('TablaUsuario')