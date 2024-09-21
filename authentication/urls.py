from django.urls import path
from .views import *

urlpatterns =[
    path('',AuthLoginpageview.as_view()),
    path('logout/',AuthLogoutpageview.as_view()),
    path('signup/',AuthSignuppageview.as_view()),
]