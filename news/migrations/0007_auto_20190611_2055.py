# Generated by Django 2.2.1 on 2019-06-11 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190610_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 20, 55, 50, 28523)),
        ),
    ]