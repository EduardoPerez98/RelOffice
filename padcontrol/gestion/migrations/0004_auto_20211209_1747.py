# Generated by Django 3.2.9 on 2021-12-09 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20211209_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficios',
            name='alcance',
        ),
        migrations.AddField(
            model_name='oficios',
            name='alcance',
            field=models.ForeignKey(blank=True, db_column='alcance', null=True, on_delete=django.db.models.deletion.PROTECT, to='gestion.oficios'),
        ),
    ]
