from .models import Pedidos,ProductoPedido
from django import forms

class CrearPedido(forms.ModelForm):
    class Meta:
        model=Pedidos
        fields=["nombre_cliente","direccion_cliente"]

class FormPedido(forms.ModelForm):
    class Meta:
        model=Pedidos
        fields=["nombre_cliente","direccion_cliente"]

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['producto', 'cantidad_producto']