from django.db import models
from customer.models import *
from product.models import *

class Order(models.Model):
    product_ref=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    customer_ref=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True)
    order_data=models.DateField(null=True)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    gst=models.FloatField(default=0)
    final_price=models.IntegerField(default=0)


