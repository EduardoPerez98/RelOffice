# Generated by Django 3.2.9 on 2022-01-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20220114_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficios',
            name='altas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='oficios',
            name='bajas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='oficios',
            name='clave_depe',
            field=models.ForeignKey(blank=True, db_column='clave_depe', null=True, on_delete=django.db.models.deletion.PROTECT, to='gestion.dependencias'),
        ),
        migrations.AddField(
            model_name='oficios',
            name='pendientes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='oficios',
            name='sustituciones',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Envios',
        ),
    ]
