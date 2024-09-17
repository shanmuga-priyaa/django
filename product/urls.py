from django.urls import path
from .views import *

urlpatterns =[
    path('home/',indexpage),
    path('about/',aboutpage),  
    path('productlist/',productlist),
    path('productadd/',productadd),
    path('proupdate/<int:id>/',productupdate,name='prod_update'),
    path('productdelete/<int:id>/',productdelete,name='prod_delete')
]