from django.urls import path
from .views import *

urlpatterns =[
    path('home/',indexpage),
    path('about/',aboutpage),  
    path('productlist/',ProductListView.as_view()),
    path('productadd/',ProductAddView.as_view()),
    path('proupdate/<int:id>/',ProductUpdateView.as_view(),name='prod_update'),
    path('prodelete/<int:id>/',ProductDeleteView.as_view(),name='prod_delete'),
]