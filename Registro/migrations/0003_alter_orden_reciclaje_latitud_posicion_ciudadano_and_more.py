# Generated by Django 4.2.1 on 2023-06-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_orden_reciclaje_latitud_posicion_recolector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='latitud_posicion_ciudadano',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='latitud_posicion_recolector',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='longitud_posicion_ciudadano',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
