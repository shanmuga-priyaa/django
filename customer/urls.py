from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('header/',header),
    path('customerlist/',customerlistView.as_view()),
    path('customeradd/',customeraddView.as_view()),
    path('customerupdate/<int:id>/',customerupdateView.as_view(),name="cust_update"),
    path('customerdelete/<int:id>/',customerdeleteView.as_view(),name="cust_delete")
]