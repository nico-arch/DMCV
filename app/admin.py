from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
@admin.register(Dossier, Diagnostic, RendezVous, Prescription)


class ViewAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Panneau d'administration DMCV"
admin.site.site_title = 'DMCV'
admin.site.index_title = "Administration"
