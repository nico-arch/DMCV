from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from typing import List
import datetime
import dateutil

# Create your views here.
def index(request):
    return render(request, 'index.html')

#from django.contrib.auth.mixins import LoginRequiredMixin
def profile(request):

  # Cherche le dossier de l'utilisateur
    dossierUtl = Dossier.objects.all().filter(utilsateur = request.user)
    dossierUtlnext = Dossier.objects.get(utilsateur = request.user)


    # Cherche la liste de diagnostics de l'utilisateur
    diagnostics_list = Diagnostic.objects.all().filter( dossier__in= dossierUtl)

    #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
    sex  = dossierUtlnext.sex
    age  = int( (date.today() - dossierUtlnext.dateDeNaissance) // timedelta(days=365.2425) )


    context = {
        'dossier': dossierUtl,
        'age': age,
        'sex': sex,
        'diagnostics': diagnostics_list,
    }

    return render(request, 'profile/index.html', context = context)
