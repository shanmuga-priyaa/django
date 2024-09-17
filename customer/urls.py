from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('header/',header),
    path('customerlist/',customerlist),
    path('customeradd/',customeradd),
    path('customerupdate/<int:id>/',customerupdate,name="cust_update"),
    path('customerdelete/<int:id>/',customerdelete,name='cust_delete')
]