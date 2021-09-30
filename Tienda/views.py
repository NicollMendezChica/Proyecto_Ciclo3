from django.shortcuts import render

# Create your views here.

def formulario(request):
    return render(request, "Formulario.html")

def TablaProductos(request):
    return render(request, "TablaProductos.html")