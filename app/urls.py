from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
]
