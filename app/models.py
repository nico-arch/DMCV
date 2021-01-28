# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.utils import timezone

import datetime
import dateutil


# Create your models here.

class Dossier(models.Model):
    """Table contenant des informations pour la création de dossiers virtuels pour les patients de la clinique."""
    #type = models.CharField(max_length=200, help_text='Edition du livre')

    utilsateur  = models.OneToOneField(User, on_delete = models.CASCADE,
    primary_key = True, help_text='')

    dateDeNaissance = models.DateField('Date de naissance', default=timezone.now, null=True, blank=True)

    SEX_VALUE = (
        ('0', 'M'),
        ('1', 'F'),
    )
    sex = models.CharField(
        'Sexe',
        max_length=1,
        choices=SEX_VALUE,
        blank=True,
        default='0',
        help_text='(1 = male; 0 = female)',
    ) 
    addresse    = models.CharField(max_length=200, null=True,help_text='Numero, Rue')
    identifiantCin_Nif = models.CharField('Cin ou Nif',max_length=200, null=True, help_text='')


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Dossier de : {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))



class Diagnostic(models.Model):
    """Table contenant les champs à remplir par le médecin lors du diagnostics"""
    dossier   = models.ForeignKey('Dossier', on_delete=models.SET_NULL, null=True)
    
    #age = (date.today() - dossier.dateDeNaissance) // timedelta(days=365.2425)
    #age = birthday(dossier.age)
    #sex = dossier.sex

    CP_VALUE = (
        ('0', 'Valeur: 0'),
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
        ('3', 'Valeur: 3'),
    )
    cp = models.CharField(
        'Chest pain type',
        max_length=1,
        choices=CP_VALUE,
        default='0',
        help_text='(4 values)',
    ) 
    
    trestbps = models.IntegerField(
      'Resting blood pressure', 
      default=130,
      help_text='Resting blood pressure (in mm Hg on admission to the hospital)')


    chol = models.IntegerField('Serum cholestoral',
    default=131, 
    help_text='mg/dl')

    FBS_VALUE = (
        ('1', '> 120 mg/dl'),
        ('0', '<= 120 mg/dl'),
    )
    fbs = models.CharField(
    'Fasting blood sugar',
    default='0',
    max_length=1,
    help_text='(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)')
    

    RESTECG_VALUE = (
        ('0', 'Niveau: 1'),
        ('1', 'Niveau: 2'),
        ('2', 'Niveau: 3'),
    )
    restecg = models.CharField(
    'Resting electrocardiographic results',
    default='0',
    max_length=13,
    help_text=' (values 0,1,2)')


    thalach = models.IntegerField(
    'Maximum heart rate achieved',
    default=174,
    help_text='')


    EXANG_VALUE = (
        ('1', 'Yes'),
        ('0', 'NO'),
    )
    exang = models.CharField(
    'Exercise induced angina',
    default='0',
    max_length=13,
    help_text='exercise induced angina (1 = yes; 0 = no)')



    oldpeak = models.CharField(
    'Oldpeak',
    max_length=13,
    default='',
    help_text='Oldpeak = ST depression induced by exercise relative to rest')

    slope = models.CharField(
    'Slope',default='',
    max_length=13,
    help_text='The slope of the peak exercise ST segment')

    ca = models.CharField(
    'Number of major vessels',
    default='',
    max_length=13,
    help_text='Number of major vessels (0-3) colored by flourosopy')

    thal = models.CharField(
    'Thal',default='',
    max_length=13, 
    help_text='Thal: 3 = normal; 6 = fixed defect; 7 = reversable defect')

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Diagnostic de : {0}'.format(self.dossier.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))



    def birthday(date):
        # Get the current date
        now = datetime.datetime.utcnow()
        now = now.date()

        # Get the difference between the current date and the birthday
        age = dateutil.relativedelta.relativedelta(now, date)
        age = age.years

        return age

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



