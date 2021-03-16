from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.
# Register your models here.
#@admin.register(Dossier, Diagnostic, RendezVous, Prescription)


#class ViewAdmin(admin.ModelAdmin):
#    pass

class RendezVousInline(admin.TabularInline):
    """Defines format of inline Diagnostic insertion (used in DossierAdmin)"""
    model = RendezVous
    extra = 0


class DiagnosticInline(admin.TabularInline):
    """Defines format of inline Diagnostic insertion (used in DossierAdmin)"""
    model = Diagnostic
    extra = 0


class DossierAdmin(admin.ModelAdmin):
    search_fields = ['utilisateur']
    list_display = ('utilisateur','dateDeNaissance','identifiantCin_Nif')
    #fields = []
    inlines = [RendezVousInline, DiagnosticInline]


admin.site.register(Dossier, DossierAdmin)


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    #list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    #list_filter = ('status', 'due_back')
    fieldsets = (
        ('---------', {
            'fields': ('date', 'cp', 'trestbps', 'chol','fbs','restecg')
        }),
        ('---------', {
            'fields': ('thalach', 'exang', 'oldpeak','slope','ca','thal')
        }),
        )


#admin.site.register(Diagnostic)
admin.site.register(RendezVous)
admin.site.register(Prescription)



admin.site.site_header = "Panneau d'administration DMCV"
admin.site.site_title = 'DMCV'
admin.site.index_title = "Administration"
