# Generated by Django 3.2.9 on 2022-01-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_alter_oficios_clave_depe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='altas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='bajas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='pendientes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='sustituciones',
            field=models.PositiveIntegerField(default=0),
        ),
    ]