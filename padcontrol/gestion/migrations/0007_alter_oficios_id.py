# Generated by Django 3.2.9 on 2021-12-10 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_alter_oficios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
