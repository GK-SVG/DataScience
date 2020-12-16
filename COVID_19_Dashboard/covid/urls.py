from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="Index"),
    path('selectCountry',drillDownACountry,name='drillDown')
]
