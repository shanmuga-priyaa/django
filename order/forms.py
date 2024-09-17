from django import forms
from .models import *
 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_ref','customer_ref','order_data','quantity']