# Generated by Django 3.2.9 on 2021-12-10 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_alter_oficios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
