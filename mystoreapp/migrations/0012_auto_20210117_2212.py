# Generated by Django 3.1 on 2021-01-17 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0011_auto_20210117_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 22, 12, 48, 479347)),
        ),
    ]
