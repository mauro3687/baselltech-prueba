# Generated by Django 4.2.2 on 2023-06-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_usuariocliente_numeracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocliente',
            name='correo',
            field=models.EmailField(default='correo@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuariocliente',
            name='fecha_nacimiento',
            field=models.DateField(default='2000/02/23'),
        ),
        migrations.AlterField(
            model_name='usuariocliente',
            name='numeracion',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
