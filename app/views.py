from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from typing import List


# Create your views here.
def index(request):
    return render(request, 'index.html')

#from django.contrib.auth.mixins import LoginRequiredMixin
def profile(request):

  # Cherche le dossier de l'utilisateur
    dossierUtl = Dossier.objects.filter(utilsateur = request.user)
    
    #diagnostics = list(Diagnostic.objects.all().filter( dossier= dossierUtl) )
    diagnostics = list(Diagnostic.objects.all())
    diagnosticCount = diagnostics.count()

    context = {
        'dossier': dossierUtl,
        'diagnostics': diagnostics,
        'count': diagnosticCount,
    }

    return render(request, 'profile/index.html', context = context)
