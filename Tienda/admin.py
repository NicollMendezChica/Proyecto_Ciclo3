from django.contrib import admin
from Tienda.models import InicioSesion,Usuario,Tienda,Movimiento,Producto

# Register your models here.

admin.site.register(InicioSesion)
admin.site.register(Usuario)
admin.site.register(Tienda)
admin.site.register(Movimiento)
admin.site.register(Producto)