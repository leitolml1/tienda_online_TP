from django.db import models

# Create your models here.

class  Categorias(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class  Productos(models.Model):
    nombre=models.CharField(max_length=150)
    descripcion=models.TextField(default="Sin descripcion")
    precio=models.FloatField()
    #imagen=models.ImageField(upload_to='productos_imagenes/')
    categoria=models.ForeignKey(Categorias,on_delete=models.SET_DEFAULT,default="Sin categoria")

    def __str__(self):
        return self.nombre

