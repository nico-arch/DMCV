from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),

]
