from django.urls import path
from .views import *

urlpatterns =[
    path('',loginpage),
    path('logout/',logoutpage),
    path('signup/',signuppage),
]