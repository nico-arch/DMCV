from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
#@admin.register(Dossier, Diagnostic, RendezVous, Prescription)


#class ViewAdmin(admin.ModelAdmin):
#    pass

class DossierAdmin(admin.ModelAdmin):
    search_fields = ['utilsateur']
    list_display = ('utilsateur','dateDeNaissance','identifiantCin_Nif')
    #fields = []
    #inlines = []

admin.site.register(Dossier, DossierAdmin)

admin.site.register(Diagnostic)
admin.site.register(RendezVous)
admin.site.register(Prescription)



admin.site.site_header = "Panneau d'administration DMCV"
admin.site.site_title = 'DMCV'
admin.site.index_title = "Administration"
