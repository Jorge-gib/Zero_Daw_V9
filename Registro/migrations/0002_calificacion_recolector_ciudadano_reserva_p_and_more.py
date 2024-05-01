# Generated by Django 4.2.1 on 2024-04-24 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion_recolector_ciudadano_reserva',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion_estrellas_ciudadano', models.FloatField(null=True)),
                ('calificacion_estrellas_recolector', models.FloatField(null=True)),
                ('opinion_servicio_ciudadano', models.CharField(max_length=400, null=True)),
                ('opinion_servicio_recolector', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='p',
            fields=[
                ('p', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion_desechos',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField()),
                ('cantidad_plastico', models.IntegerField(default=0)),
                ('cantidad_vidrio', models.IntegerField(default=0)),
                ('cantidad_carton', models.IntegerField(default=0)),
                ('cantidad_aluminio', models.IntegerField(default=0)),
                ('cantidad_metal', models.IntegerField(default=0)),
                ('cantidad_electrodomesticos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion_desechos_reserva',
            fields=[
                ('id_registro_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField()),
                ('cantidad_plastico', models.IntegerField(default=0)),
                ('cantidad_vidrio', models.IntegerField(default=0)),
                ('cantidad_carton', models.IntegerField(default=0)),
                ('cantidad_aluminio', models.IntegerField(default=0)),
                ('cantidad_metal', models.IntegerField(default=0)),
                ('cantidad_electrodomesticos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
                ('total_material_reciclado', models.IntegerField(default=0)),
                ('monto_pago', models.IntegerField(default=0)),
                ('id_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.recepcion_desechos')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_pago_reserva',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
                ('total_material_reciclado', models.IntegerField(default=0)),
                ('monto_pago', models.IntegerField(default=0)),
                ('id_registro_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.recepcion_desechos_reserva')),
            ],
        ),
        migrations.RemoveField(
            model_name='registro_entrega_material',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='orden_reciclaje',
            name='cantidad_material',
        ),
        migrations.RemoveField(
            model_name='orden_reciclaje',
            name='tipo_material',
        ),
        migrations.RemoveField(
            model_name='reserva_orden',
            name='cantidad_material',
        ),
        migrations.RemoveField(
            model_name='reserva_orden',
            name='tipo_material',
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_aluminio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_carton',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_electrodomesticos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_metal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_plastico',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='cantidad_vidrio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='estado',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='latitud_posicion_recolector',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='orden_reciclaje',
            name='longitud_posicion_recolector',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_aluminio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_carton',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_electrodomesticos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_metal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_plastico',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='cantidad_vidrio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva_orden',
            name='estado',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usermodelo',
            name='comuna',
            field=models.CharField(default='escribe tu comuna', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodelo',
            name='validacion_recolector',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='calificacion_recolector_ciudadano',
            name='calificacion_estrellas_ciudadano',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='calificacion_recolector_ciudadano',
            name='calificacion_estrellas_recolector',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='calificacion_recolector_ciudadano',
            name='opinion_servicio_ciudadano',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='calificacion_recolector_ciudadano',
            name='opinion_servicio_recolector',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='latitud_posicion_ciudadano',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='orden_reciclaje',
            name='longitud_posicion_ciudadano',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='latitud_posicion_ciudadano',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='latitud_posicion_recolector',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='longitud_posicion_ciudadano',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='reserva_orden',
            name='longitud_posicion_recolector',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='usermodelo',
            name='direccion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usermodelo',
            name='licencia_automotriz',
            field=models.ImageField(blank=True, null=True, upload_to='licencias/'),
        ),
        migrations.DeleteModel(
            name='Calificacion_reciclador',
        ),
        migrations.DeleteModel(
            name='Registro_entrega_material',
        ),
        migrations.AddField(
            model_name='recepcion_desechos_reserva',
            name='id_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.reserva_orden'),
        ),
        migrations.AddField(
            model_name='recepcion_desechos',
            name='id_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.orden_reciclaje'),
        ),
        migrations.AddField(
            model_name='calificacion_recolector_ciudadano_reserva',
            name='id_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.reserva_orden'),
        ),
    ]