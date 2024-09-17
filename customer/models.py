from django.db import models
from product.models import *
class customer(models.Model):
    full_name=models.CharField(max_length=200,null=True)
    mobile_number=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    age=models.IntegerField(default=0)

    product_ref = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.full_name