# Generated by Django 3.0.6 on 2020-05-14 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200513_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='in_cart',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 14, 11, 50, 8, 355137), verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 14, 11, 50, 8, 355645), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 11, 50, 8, 356278), verbose_name='Released'),
        ),
    ]