from django.shortcuts import render,redirect,get_object_or_404
from .models import Pedidos,ProductoPedido
from .forms import FormPedido,ProductoPedidoForm,CrearPedido
# Create your views here.

def pedidos(request):
    pedidos=Pedidos.objects.all()
    for pedido in pedidos:
        # Calcula el total para cada pedido
        pedido.total_pedido = sum(producto_pedido.subtotal() for producto_pedido in pedido.productos_pedido_set.all())
    return render(request,"pedidos.html",{
        "pedidos":pedidos
    })
def crearPedido(request):
    id=None
    if request.method=="POST":
        form=CrearPedido(request.POST)
        if form.is_valid():
            nuevoPedido=form.save(commit=False)
            nuevoPedido.save()
            id=nuevoPedido.id

        return redirect("agregarProductos",id=id)
    else:
        return render(request,"crearPedido.html",{
            "form":CrearPedido(),
        })
def eliminarPedido(request,id):
    pedido=get_object_or_404(Pedidos,id=id)
    if request.method=="POST":
        pedido.delete()
        return redirect("pedidos")
    else:
        return render(request,"eliminarPedido.html",{

        })
def editarPedido(request,id):
    pedido=get_object_or_404(Pedidos,id=id)
    pedido.total_pedido = sum(producto_pedido.subtotal() for producto_pedido in pedido.productos_pedido_set.all())
    productosXpedido=ProductoPedido.objects.filter(pedido=pedido)
    if request.method=="GET":
        instanciar_pedido=FormPedido(instance=pedido)
        return render(request,"editarPedido.html",{
            "productosXpedido":productosXpedido,
            "pedido":pedido,
            "form":instanciar_pedido,
            "ProductoPedidoForm":ProductoPedidoForm(),
            "id":pedido.id
            })
    else:
        instanciar_pedido=FormPedido(request.POST,instance=pedido)
        if instanciar_pedido.is_valid():
            instanciar_pedido.save()
            return redirect("pedidos")
def eliminar_producto_pedido(request, id):
    print(f"Intentando eliminar el producto con ID {id}")
    pedido_producto = get_object_or_404(ProductoPedido, id=id)
    print(f"Producto encontrado: {pedido_producto}")
    
    if request.method == "POST":
        pedido_producto.delete()
        print(f"Producto {id} eliminado")
        
        pedido_id = pedido_producto.pedido.id
        pedido = Pedidos.objects.get(id=pedido_id)
        pedido.total_pedido = sum(producto.subtotal() for producto in pedido.productos_pedido_set.all())
        pedido.save()
        
        return redirect('editarPedido', id=pedido_id)

def agregarProductoPedido(request,id):
    pedido = get_object_or_404(Pedidos, id=id)
    
    if request.method == "POST":
        form = ProductoPedidoForm(request.POST)
        if form.is_valid():
            producto_pedido = form.save(commit=False)
            producto_pedido.pedido = pedido
            producto_pedido.save()
            return redirect('editarPedido', id=pedido.id)
    return redirect('editarPedido', id=pedido.id)