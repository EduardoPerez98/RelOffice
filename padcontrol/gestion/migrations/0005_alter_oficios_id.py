# Generated by Django 3.2.9 on 2021-12-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20211209_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
