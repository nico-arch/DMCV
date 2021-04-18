from django.contrib import admin
from .models import *
from sendsms import api
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from datetime import date


#from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
#@admin.register(Dossier, Diagnostic, RendezVous, Prescription)


#class ViewAdmin(admin.ModelAdmin):
#    pass


#def Sms(modelddmin, request, queryset):
#    for qs in queryset:
#        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

 #       print(selected)
        #selected = queryset.values_list('pk', flat=True)
        #if selected > '0':
        #   print(selected)

        #api.send_sms(body='I can haz txt', from_phone='+41791111111', to=['+41791234567'])


def send_sms(modeladmin, request, queryset):

    fromPhoneNumber ='+50900000000'
    for obj in queryset:
        #Rendevous est aujoud'hui
        if date.today() == obj.GetDate():
           api.send_sms(body='Chèr(e) client(e) vous avez un rendevous aujourd\'hui a la clinique à '+str(h1) +'.', from_phone=fromPhoneNumber, to=[str(obj.GetPhoneNumber())])

        #Rendevous est pour l'avenir
        if date.today() < obj.GetDate():
           d1 =  obj.GetDate()
           h1 =  obj.GetHour()

           d2 = date.today()

           result = (d1-d2).days//7


           #Alert 1 day before the Rendezvous
           dayCondition = 1
           if ((result == 0) and (d1.isoweekday() == d2.isoweekday()+dayCondition )) or ((result == 0) and (d1.isoweekday() == d2.isoweekday()-6)):
              #api.send_sms(body= 'result = '+str(result)+' d1.isoweekday() ='+ str(d1.isoweekday())+' d2.isoweekday()+dayCondition = '+str(d2.isoweekday()+dayCondition )+'  Chèr(e) client(e) vous avez un rendez-vous dans '+str(dayCondition)+' jour(s) à la clinique.', from_phone=fromPhoneNumber, to=[str(obj.GetPhoneNumber())])
              api.send_sms(body=  'Chèr(e) client(e) vous avez un rendez-vous dans '+str(dayCondition)+' jour(s) à la clinique à '+str(h1) +'.', from_phone=fromPhoneNumber, to=[str(obj.GetPhoneNumber())])
              #print("Date today is < than the RendezVous date, Week between: ", result,"\n -------------------------------------------------------")
              #print("Rendevous day =", d1.isoweekday() )
              #print("Today day =", d2.isoweekday() )


           #Alert 1 week before the Rendezvous
           weekCondition = 1
           if (result == weekCondition) and (d1.isoweekday() == d2.isoweekday()):
              api.send_sms(body='Chèr(e) client(e) vous avez un rendez-vous dans '+str(weekCondition)+' semaine(s) à la clinique à '+str(h1) +'.', from_phone=fromPhoneNumber, to=[str(obj.GetPhoneNumber())])
              #print("Date today is < than the RendezVous date, Week between: ", result,"\n -------------------------------------------------------")
              #print("Rendevous day =", d1.isoweekday() )
              #print("Today day =", d2.isoweekday() )




def supprimer_les_anciens_rendezvous(modeladmin, request, queryset):
    to_be_deleted = []
    for obj in queryset:
        #RendezVous passe
        if date.today() > obj.GetDate():
           print("Date today is > than the RendezVous date")
           to_be_deleted.append(obj.pk)

    queryset.filter(pk__in=to_be_deleted).delete()


class RendezVousInline(admin.TabularInline):
    """Defines format of inline Diagnostic insertion (used in DossierAdmin)"""
    model = RendezVous
    extra = 0


class DiagnosticInline(admin.TabularInline):
    """Defines format of inline Diagnostic insertion (used in DossierAdmin)"""
    model = Diagnostic
    extra = 0


class DossierAdmin(admin.ModelAdmin):
    search_fields = ['utilisateur__username']
    list_display = ('utilisateur','dateDeNaissance','identifiantCin_Nif')
    #fields = []
    inlines = [RendezVousInline, DiagnosticInline]
#    actions = [Sms]

admin.site.register(Dossier, DossierAdmin)




class PrescriptionInline(admin.TabularInline):
    """Defines format of inline Diagnostic insertion (used in DossierAdmin)"""
    model = Prescription
    extra = 0



@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('__str__','dossier','date')
    search_fields = ['dossier__utilisateur__username']
    inlines = [PrescriptionInline]
    fieldsets = (
        ('---------', {
            'fields': ('dossier','date', 'cp', 'trestbps', 'chol','fbs','restecg')
        }),
        ('---------', {
            'fields': ('thalach', 'exang', 'oldpeak','slope','ca','thal')
        }),
        )
#admin.site.register(Diagnostic)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('__str__','diagnostic','notesImportantes')
    search_fields = ['diagnostic__dossier__utilisateur__username']


#admin.site.register(Prescription)


@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('__str__','dossier','date','Heure')
    search_fields = ['dossier__utilisateur__username']
    actions = [send_sms, supprimer_les_anciens_rendezvous]


#admin.site.register(RendezVous)




admin.site.site_header = "Panneau d'administration CLCB"
admin.site.site_title = 'CLCB'
admin.site.index_title = "Administration"
