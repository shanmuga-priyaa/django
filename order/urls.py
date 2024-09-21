from django.urls import path
from .views import *

urlpatterns = [
        path('orderadd/',orderaddview.as_view()),
        path('orderlist/',orderlistView.as_view()),
        path('orderupdate/<int:id>/',orderupdateview.as_view(),name='ord_update'),
        path('orderdelete/<int:id>/',orderdeleteview.as_view(),name='ord_delete')
]