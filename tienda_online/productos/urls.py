from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos,name="productos"),
    path('agregarProducto',views.agregarProducto,name="agregarProducto"),
    path('eliminarProducto/<int:id>',views.eliminarProducto,name="eliminarProducto"),
    path('editarProducto/<int:id>',views.editarProducto,name="editarProducto"),
]
