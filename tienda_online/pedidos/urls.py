from django.urls import path
from . import views
urlpatterns = [
    path('', views.pedidos,name="pedidos"),
    path('crearPedido/', views.crearPedido,name="crearPedido"),

    path('editarPedido/<int:id>', views.editarPedido,name="editarPedido"),
    path('agregarProductos/<int:id>', views.agregarProductoPedido,name="agregarProductos"),


    path('eliminarPedido/<int:id>', views.eliminarPedido,name="eliminarPedido"),
    path('agregarProductoPedido/<int:id>', views.agregarProductoPedido,name="agregarProductoPedido"),
    path('eliminar_producto_pedido/<int:id>', views.eliminar_producto_pedido,name="eliminar_producto_pedido"),



]