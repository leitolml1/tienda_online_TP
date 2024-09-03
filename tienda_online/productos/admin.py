from django.contrib import admin
from productos.models import Categorias,Productos
from pedidos.models import Pedidos,ProductoPedido

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Productos)

admin.site.register(Pedidos)
admin.site.register(ProductoPedido)

