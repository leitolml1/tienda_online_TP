# Generated by Django 5.0.2 on 2024-09-01 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pedido',
            new_name='Pedidos',
        ),
    ]
