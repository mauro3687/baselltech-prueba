# Generated by Django 4.2.2 on 2023-06-29 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subir_proyecto_precio_subir_proyecto_repositorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subir_proyecto',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usuariocliente'),
        ),
    ]
