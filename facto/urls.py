from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facto',views.facto, name='facto')
]