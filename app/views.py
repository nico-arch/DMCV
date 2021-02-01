from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from typing import List
import datetime
import dateutil

# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'profile/full-screen-table.html')



#from django.contrib.auth.mixins import LoginRequiredMixin

# to make sure that only logged-in users can access the view.
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

  # Cherche le dossier de l'utilisateur
    dossierUtl = Dossier.objects.all().filter(utilsateur = request.user)


    try:
        dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
        #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)


        # Cherche la liste de diagnostics de l'utilisateur
        diagnostics_list = Diagnostic.objects.all().filter( dossier__in= dossierUtl)

        #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
        sex  = dossierUtlnext.sex
        #age  = int( (date.today() - dossierUtlnext.dateDeNaissance) // timedelta(days=365.2425) )


        context = {
            'dossier': dossierUtl,
            #'age': age,
            'sex': sex,
            'diagnostics': diagnostics_list,
        }

        return render(request, 'profile/index.html', context = context)

    except:
        context = {
        'dossier': 'error',
        #'age': 'error',
        'sex': 'error',
        'diagnostics': False,
        }
        return render(request, 'profile/index.html', context = context)

    
