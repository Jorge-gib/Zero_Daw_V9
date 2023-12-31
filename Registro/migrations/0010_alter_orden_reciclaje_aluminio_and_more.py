# Generated by Django 4.2.1 on 2023-08-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_rename_cantidad_material_orden_reciclaje_aluminio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='aluminio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='carton',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='plastico',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='vidrio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro_entrega_material',
            name='aluminio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro_entrega_material',
            name='carton',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro_entrega_material',
            name='plastico',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro_entrega_material',
            name='vidrio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='aluminio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='carton',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='plastico',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='vidrio',
            field=models.IntegerField(default=0),
        ),
    ]
