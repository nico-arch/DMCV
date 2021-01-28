# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Dossier(models.Model):
    """Table contenant des informations pour la création de dossiers virtuels pour les patients de la clinique."""
    #type = models.CharField(max_length=200, help_text='Edition du livre')

    utilsateur  = models.OneToOneField(User, on_delete = models.CASCADE,
    primary_key = True, help_text='')

    addresse    = models.CharField(max_length=200, null=True,help_text='Numero, Rue')
    identifiantCin_Nif = models.CharField(max_length=200, null=True, help_text='')


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Dossier de : {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))



class Diagnostic(models.Model):
    """Table contenant les champs à remplir par le médecin lors du diagnostics"""
    dossier   = models.ForeignKey('Dossier', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Diagnostic de : {0}'.format(self.dossier.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))


class Prescription(models.Model):
    """Table contenant les prescriptions et les notes essentielles pour les patients."""

    diagnostic   = models.OneToOneField('Diagnostic', on_delete=models.CASCADE, primary_key = True, help_text='')
    ordonnance = models.CharField(max_length=500, help_text='')
    notesImportantes = models.CharField(max_length=200, help_text='')

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Prescription de :{0}'.format(self.diagnostic.dossier.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))



class RendezVous(models.Model):
    """Table contenant des informations pour la configuration des rendez-vous"""
    dossier   = models.ForeignKey('Dossier', on_delete=models.SET_NULL, null=True)
    date     = models.DateField(null=True, blank=True)

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'RendezVous de :{0} ______ le : {1} (Année - Mois - Jour)'.format(self.dossier.utilsateur.username, self.date)
        #return '{0} ({1})'.format(self.id,self.book.title))



