# Generated by Django 2.2.1 on 2019-06-10 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190610_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 10, 11, 59, 18, 202745)),
        ),
    ]
