# Generated by Django 4.2.5 on 2024-03-03 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_rename_owner_name_shop_shop_name_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_in_stock',
        ),
    ]