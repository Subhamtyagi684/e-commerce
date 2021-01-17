# Generated by Django 3.1 on 2021-01-16 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0003_auto_20210116_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prod_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_type',
            field=models.CharField(choices=[('clothing', 'Clothing'), ('bags', 'Bags & luggage'), ('footwear', 'Footwear'), ('electronics', 'Electronics'), ('beauty_grocery', 'Beauty & Grocery'), ('sports', 'Sports'), ('books', 'Books'), ('baby', 'Baby Products')], help_text='choose one from [clothing, bags, footwear, electronics, beauty_grocery, sports, books, baby]', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 14, 52, 54, 735164)),
        ),
    ]
