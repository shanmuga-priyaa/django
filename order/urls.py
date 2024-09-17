from django.urls import path
from .views import *

urlpatterns = [
    path('orderadd/',orderadd),
     path('orderadd/',orderadd),
     path('orderlist/',orderlist),
    path('orderupdate/<int:id>/',orderupdate,name='ord_update'),
    path('orderdelete/<int:id>/',orderdelete,name='ord_delete')
]