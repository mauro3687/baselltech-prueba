# Generated by Django 4.2.2 on 2023-06-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_usuariocliente_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocliente',
            name='correo',
            field=models.CharField(default='correo@example.com', max_length=100),
        ),
    ]
