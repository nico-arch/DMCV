from django import forms
from .models import *


class DiagnosticForm(forms.ModelForm):
    name = "Diagnostic"
    class Meta:
        model = Diagnostic
        fields =('date', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal')
