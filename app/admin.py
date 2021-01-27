from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
@admin.register(Dossier, Diagnostic, RendezVous, Prescription)


class ViewAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = 'DMCV Administration Panel'
admin.site.site_title = 'DMCV'

