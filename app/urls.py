from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('profileRendezVous/', profileRendezVous, name='profileRendezVous'),
    path(r'view_diagnostic/(?<pk>\d+)$', view_diagnostic, name='view_diagnostic'),
    path('test/', test, name='test'),
]
