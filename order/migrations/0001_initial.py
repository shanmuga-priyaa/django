# Generated by Django 4.2.15 on 2024-09-04 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_rename_product_name_product_model_name'),
        ('customer', '0002_customer_product_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_data', models.DateField(null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('gst', models.FloatField(default=0)),
                ('final_price', models.IntegerField(default=0)),
                ('customer_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
                ('product_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
        ),
    ]
