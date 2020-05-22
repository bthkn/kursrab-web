# Generated by Django 2.2.7 on 2019-12-08 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('content', models.TextField(verbose_name='Content')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 8, 15, 4, 15, 155601), verbose_name='Posted')),
            ],
            options={
                'verbose_name': 'Blog page',
                'verbose_name_plural': 'Blog page',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
