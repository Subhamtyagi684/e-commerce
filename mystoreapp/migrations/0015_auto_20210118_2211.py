# Generated by Django 3.1 on 2021-01-18 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0014_auto_20210118_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 22, 11, 57, 632812)),
        ),
    ]
