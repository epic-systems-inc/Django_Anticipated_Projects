from django import forms
from .models import AnticipatedProject

class ProjectForm(forms.ModelForm):
    #def add_forecast_months():
        
    class Meta:
        model = AnticipatedProject
        fields = ['salesleadid', 'cash_flow_responsible', 'project_name', 'client_name', 
                  'subjective_probability', 'model_probability']