# Generated by Django 4.2.1 on 2024-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_registro_pago_telefono_reciclador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodelo',
            name='tipo_usuario',
            field=models.CharField(choices=[('Recolector', 'Recolector'), ('Reciclador', 'Reciclador'), ('Ciudadano', 'Ciudadano'), ('Operario municipalidad', 'Operario municipalidad')], max_length=200, null=True),
        ),
    ]