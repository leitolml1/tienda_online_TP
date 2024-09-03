from django.db import models
from datetime import datetime
from productos.models import Productos # Traido desde mi carpeta "productos"

class  Pedidos(models.Model):
    fecha_pedido=models.DateField(auto_now=datetime)
    nombre_cliente=models.CharField(max_length=100)
    direccion_cliente=models.CharField(max_length=300)
    total_pedido=models.FloatField(default=0)
    productos_pedido = models.ManyToManyField(Productos, through='ProductoPedido')

    def __str__(self):
        return f"NRO PEDIDO:{self.id},NOMBRE_CLIENTE:{self.nombre_cliente}"



class  ProductoPedido(models.Model):
    producto=models.ForeignKey(Productos,on_delete=models.SET_DEFAULT,default=1,related_name='pedidos_producto')
    pedido=models.ForeignKey(Pedidos,on_delete=models.CASCADE,default=1,related_name='productos_pedido_set')
    cantidad_producto=models.IntegerField(default=0)

    def subtotal(self):# Funcion para calcular el precio total del producto x cantidad seleccionada 
        return self.producto.precio * self.cantidad_producto

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad_producto} en Pedido: {self.pedido.id}"

