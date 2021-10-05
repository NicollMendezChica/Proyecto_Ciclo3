from django import forms
from Tienda.models import *

class ProductoFrm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'                # fields=('nomProd', 'Precio', 'Color',)

class UsuarioFrm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'