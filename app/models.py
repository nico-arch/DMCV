# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.utils import timezone

from app.ml import *

import datetime
import dateutil

from django.shortcuts import render, redirect, get_object_or_404

# Create your models here.


class Dossier(models.Model):
    """Table contenant des informations pour la création de dossiers virtuels pour les patients de la clinique."""

    utilisateur = models.OneToOneField(User,
                                      on_delete=models.CASCADE,
                                      primary_key=True,
                                      help_text='')

    dateDeNaissance = models.DateField('Date de naissance',
                                       default=timezone.now,
                                       null=False,
                                       blank=False)

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
        help_text='(0 = male; 1 = female)',#a corriger################################################
    )
    phone = models.CharField(
        'Téléphone',
        max_length=200,
        default='',
        help_text='xxx xx xx xxxx'
        )

    addresse = models.CharField(max_length=200,
                                null=True,
                                help_text='Numero, Rue')

    identifiantCin_Nif = models.CharField('Cin ou Nif',
                                          max_length=200,
                                          null=True,
                                          help_text='')
    class Meta:
        ordering = ['utilisateur']


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return '{0}'.format(self.utilisateur.username)

        #return 'Dossier de : {0}'.format(self.utilisateur.username)


class Diagnostic(models.Model):
    """Table contenant les champs à remplir par le médecin lors du diagnostics"""
    dossier = models.ForeignKey('Dossier',
                                on_delete=models.CASCADE,
            )

    #age = (date.today() - dossier.dateDeNaissance) // timedelta(days=365.2425)
    #age = birthday(dossier.age)
    #sex = dossier.sex
    date = models.DateField('Date du diagnostic',
                                       default=timezone.now,
                                       null=False,
                                       blank=False)
    CP_VALUE = (
        ('0', 'Valeur: 0'),
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
        ('3', 'Valeur: 3'),
    )
    cp = models.CharField(
        'Chest pain type',
        max_length=13,
        choices=CP_VALUE,
        default='1',
        help_text='(4 values)',
    )

    trestbps = models.IntegerField(
        'Resting blood pressure',
        default=130,
        help_text=
        'Resting blood pressure (in mm Hg on admission to the hospital)')

    chol = models.IntegerField('Serum cholestoral',
                               default=236,
                               help_text='mg/dl')

    FBS_VALUE = (
        ('1', '> 120 mg/dl'),
        ('0', '<= 120 mg/dl'),
    )
    fbs = models.CharField(
        'Fasting blood sugar',
        default='0',
        max_length=13,
        choices=FBS_VALUE,
        help_text='(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)')

    RESTECG_VALUE = (
        ('0', 'Valeur: 0'),
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
    )
    restecg = models.CharField('Resting electrocardiographic results',
                               default='0',
                               choices=RESTECG_VALUE,
                               max_length=13,
                               help_text=' (values 0,1,2)')

    thalach = models.IntegerField('Maximum heart rate achieved',
                                  default=174,
                                  help_text='')

    EXANG_VALUE = (
        ('1', 'Yes'),
        ('0', 'NO'),
    )
    exang = models.CharField(
        'Exercise induced angina',
        default='0',
        choices=EXANG_VALUE,
        max_length=13,
        help_text='exercise induced angina (1 = yes; 0 = no)')

    oldpeak = models.DecimalField(
        'Oldpeak',
        max_digits=2,
        decimal_places=1,
        default=0.0,
        help_text='Oldpeak = ST depression induced by exercise relative to rest'
    )

    SLOPE_VALUE = (
        ('0', 'Valeur: 0'),
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
    )

    slope = models.CharField(
        'Slope',
        default='1',
        choices=SLOPE_VALUE,
        max_length=13,
        help_text='The slope of the peak exercise ST segment')

    CA_VALUE = (
        ('0', 'Valeur: 0'),
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
        ('3', 'Valeur: 3'),
    )

    ca = models.CharField(
        'Number of major vessels',
        default='1',
        choices=CA_VALUE,
        max_length=13,
        help_text='Number of major vessels (0-3) colored by flourosopy')

    THAL_VALUE = (
        ('1', 'Valeur: 1'),
        ('2', 'Valeur: 2'),
        ('3', 'Valeur: 3'),
    )
    thal = models.CharField(
        'Thal',
        default='2',
        choices=THAL_VALUE,
        max_length=13,
        help_text='Thal: 3 = normal; 6 = fixed defect; 7 = reversable defect')

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""

        ml = MachineLearning()
        #age  = int( (date.today() - self.dossier.dateDeNaissance) // timedelta(days=365.2425) )
        age  = int( (self.date - self.dossier.dateDeNaissance) // timedelta(days=365.2425) )



        #age = self.birthday(self.dossier.dateDeNaissance)
        return 'Diagnostic de : {0} Prediction : {1}'.format(
            self.dossier.utilisateur.username,
            ml.predict(age, self.dossier.sex, self.cp, self.trestbps,
                       self.chol, self.fbs, self.restecg, self.thalach,
                       self.exang, self.oldpeak, self.slope, self.ca,
                       self.thal))

    def birthday(self, date):
        # Get the current date
        now = datetime.datetime.utcnow()
        now = now.date()

        # Get the difference between the current date and the birthday
        age = dateutil.relativedelta.relativedelta(now, date)
        age = age.years

        return age


class Prescription(models.Model):
    """Table contenant les prescriptions et les notes essentielles pour les patients."""
    diagnostic = models.OneToOneField('Diagnostic',
                                      on_delete=models.CASCADE,
                                      primary_key=True,
                                      help_text='')
    ordonnance = models.CharField(max_length=500, help_text='')
    notesImportantes = models.CharField('Notes importantes',max_length=200, help_text='')

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return 'Prescription de : {0}'.format(
            self.diagnostic.dossier.utilisateur.username)


class RendezVous(models.Model):
    """Table contenant des informations pour la configuration des rendez-vous"""

    dossier = models.ForeignKey('Dossier',
                                on_delete=models.CASCADE,
                                )
    date = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return 'Rendez Vous de : {0}'.format(self.dossier.utilisateur.username)
    
    def GetDate(self):
      
        return self.date

    def GetPhoneNumber(self):
        do = get_object_or_404(Dossier, pk=self.dossier.pk)

        return do.phone