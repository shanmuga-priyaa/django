from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'