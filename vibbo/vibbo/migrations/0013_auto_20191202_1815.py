# Generated by Django 2.2.5 on 2019-12-02 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibbo', '0012_auto_20191127_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 2, 18, 15, 42, 650725)),
        ),
    ]