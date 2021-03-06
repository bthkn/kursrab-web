# Generated by Django 3.0.6 on 2020-05-21 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20200521_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 21, 1, 16, 10, 374751), verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 21, 1, 16, 10, 375246), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 1, 16, 10, 375847), verbose_name='Released'),
        ),
    ]
