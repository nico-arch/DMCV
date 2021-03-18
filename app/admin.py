from django.contrib import admin
from .models import *
from sendsms import api

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


#def send_sms(modelddmin, request, queryset):
#    #queryset.update()
#    complete_task.short_description = 'Tache effectuee'




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
            'fields': ('date', 'cp', 'trestbps', 'chol','fbs','restecg')
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
    list_display = ('__str__','dossier','date')
    search_fields = ['dossier__utilisateur__username']
#admin.site.register(RendezVous)




admin.site.site_header = "Panneau d'administration DMCV"
admin.site.site_title = 'DMCV'
admin.site.index_title = "Administration"
