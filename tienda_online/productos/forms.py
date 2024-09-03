from .models import Productos
from django import forms


class AgregarProducto(forms.ModelForm):
    class Meta:
        model=Productos
        fields=["nombre","descripcion","precio","categoria"]