# Generated by Django 2.2.5 on 2019-11-27 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibbo', '0009_auto_20191127_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 27, 9, 54, 35, 36565)),
        ),
    ]
