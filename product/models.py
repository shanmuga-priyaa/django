from django.db import models

class Product(models.Model):
    brand_name=models.CharField(max_length=200,null=True)
    model_name=models.CharField(max_length=200,null=True)
    price=models.IntegerField(default=0)
    gst=models.FloatField(default=0)
    final_price=models.IntegerField(default=0)
    picture=models.ImageField(null=True,upload_to="Images/")

    def __str__(self):
        return self.brand_name + " " + self.model_name
    

    