from django.urls import path

from .views import *

urlpatterns = [
    path('',mainpage),
    path('cats/<int:catid>/',categories),
]
