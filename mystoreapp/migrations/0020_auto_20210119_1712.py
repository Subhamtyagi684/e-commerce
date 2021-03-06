# Generated by Django 3.1 on 2021-01-19 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0019_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(default='static/images/noimage.jpg', upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 17, 12, 10, 129958)),
        ),
    ]
