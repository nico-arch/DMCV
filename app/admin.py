from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
@admin.register(Dossier, Diagnostic, RendezVous, Prescription)

#class ViewAdmin(admin.ModelAdmin):
#    pass

class ViewAdmin(ImportExportModelAdmin):
    pass
