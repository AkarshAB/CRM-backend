# Generated by Django 4.2.5 on 2024-03-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_product_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]