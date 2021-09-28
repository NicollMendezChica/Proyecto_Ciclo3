from django.db import models

# Create your models here. //Tablas espejo.

class Tienda(models.Model):
    idTienda=models.PositiveSmallIntegerField(null=False, primary_key=True)
    nombre=models.CharField(null=False, max_length=100)
    direccion=models.CharField(null=False, max_length=200)

class Usuario(models.Model):
    idUsuario=models.PositiveSmallIntegerField(primary_key=True, null=False)
    nombre=models.CharField(max_length=100, null=False)
    contraseña=models.CharField(max_length=20, null=False)
    idTienda=models.ForeignKey(Tienda, null=False)

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, null=False)
    idTienda=models.ForeignKey(Tienda, null=False)
    nombreProducto=models.CharField(max_length=50,null=False)
    stockActual=models.PositiveSmallIntegerField(null=False)
    stockMinimo=models.PositiveSmallIntegerField(null=False)
    valorUnitario=models.PositiveSmallIntegerField(null=False)
    categoria=models.CharField(max_length=50,null=False)

class InicioSesion(models.Model):
    idSesion=models.AutoField(primary_key=True, null=False)
    idUsuario=models.ForeignKey(Usuario, null=False)
    fecha=models.CharField(max_length=20, null=False)
    hora=models.CharField(max_length=10, null=False)
    descripcion=models.CharField(max_length=200, null=False)

class Movimiento(models.Model):
    idMovimientos=models.AutoField(primary_key=True, null=False)
    idTienda=models.ForeignKey(Tienda, null=False)
    tipoMovimiento=models.CharField(max_length=20, null=False)
    idProducto=models.ForeignKey(Producto, null=False)
    cantidadProducto=models.PositiveSmallIntegerField(null=False)
    descripcion=models.CharField(null=False, max_length=200)
    fecha=models.CharField(null=False, max_length=20)
    hora=models.CharField(null=False, max_length=10)
    valorTotal=models.PositiveSmallIntegerField(null=False)