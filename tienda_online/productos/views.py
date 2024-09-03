from django.shortcuts import render,get_object_or_404,redirect
from .models import Productos
from .forms import AgregarProducto
# Create your views here.


def productos(request):
    productos=Productos.objects.all()
    return render(request,"productos.html",{
        "productos":productos,

    })

def agregarProducto(request):
    if request.method=="POST":
        form=AgregarProducto(request.POST)
        if form.is_valid():
            nuevoProducto=form.save(commit=False)
            nuevoProducto.save()
        return redirect("productos")
    elif request.method=="GET":
        return render(request,"agregar_producto.html",{
            "form":AgregarProducto()
        })

def eliminarProducto(request,id):
    producto=get_object_or_404(Productos,id=id)
    if request.method=="POST":
        producto.delete()
        return redirect("productos")
    else:
        return render(request,"eliminar_producto.html",{

        })

def editarProducto(request,id):
    producto=get_object_or_404(Productos,id=id)
    if request.method=="POST":
        instanciar_producto=AgregarProducto(request.POST,instance=producto)
        if instanciar_producto.is_valid():
            instanciar_producto.save()
            return redirect("productos")
    else:
        instanciar_producto=AgregarProducto(instance=producto)
    return render(request,"editar_producto.html",{
        "form":instanciar_producto
    })