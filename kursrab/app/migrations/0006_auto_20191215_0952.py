# Generated by Django 2.2.7 on 2019-12-15 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191215_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 15, 9, 52, 12, 726339), verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 15, 9, 52, 12, 726339), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 9, 52, 12, 726339), verbose_name='Released'),
        ),
    ]