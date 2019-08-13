from django import forms
from .models import AnticipatedProject
from datetime import datetime, timedelta
from dateutil.relativedelta import *

#**************************************************************
# The desire is to have an editable grid with two parts: one corresponding the the AnticipatedProjects model and one to the Forecasts model
# The table headers should look something like the following:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sales Lead ID | Cash Flow Reponsibility | Client Name | Project Alias | Subjective Probability | Model Probability | month_previous | month_current | month_one_ahead | ... | month_twelve_ahead | Total | Notes
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The table headers for month_* should change in relation to the current month. The form data should follow suit.
# The submitted data for AnticipatedProjects formset maps directly to the AnticipatedProjects model, but it's a little more tricky for Forecasts.
# When a user submits the form data, forecasts should save each field to a new row e.g. the month_previous and the amount to row n, month_current and amount to row n+1, etc.
# The month will save to the DateAnticipated field and the entered amount will save to AnticipatedAmount. Per submit, 14 rows need to be created in the table.
#**************************************************************
class AnticipatedAwardForm(forms.Form):
    cash_flow_responsiblity = forms.CharField()
    subjective_probability = forms.IntegerField()
    notes = forms.Textarea()