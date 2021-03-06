# Generated by Django 3.2.9 on 2022-01-14 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_oficios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envios',
            name='altas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='bajas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='pendientes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='envios',
            name='sustituciones',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='alcance',
            field=models.ForeignKey(blank=True, db_column='alcance', default='Envío único', null=True, on_delete=django.db.models.deletion.PROTECT, to='gestion.oficios'),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='n_pads',
            field=models.PositiveIntegerField(),
        ),
    ]
