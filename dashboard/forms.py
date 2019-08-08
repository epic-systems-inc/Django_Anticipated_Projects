from django.forms import inlineformset_factory, MultiWidget, MultiValueField, NumberInput, CharField
from .models import AnticipatedProject, Saleslead
from datetime import datetime, timedelta
from dateutil.relativedelta import *

#**************************************************************
# The desire is to have a formset with two parts: one corresponding the the AnticipatedProjects model and one to the Forecasts model
# The table headers should look something like the following:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sales Lead ID | Cash Flow Reponsibility | Client Name | Project Alias | Subjective Probability | Model Probability | month_previous | month_current | month_one_ahead | ... | month_twelve_ahead | Total | Notes
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The table headers for month_* should change in relation to the current month. The form data should follow suit.
# The submitted data for AnticipatedProjects formset maps directly to the AnticipatedProjects model, but it's a little more tricky for Forecasts.
# When a user submits the form data, forecasts should save each field to a new row e.g. the month_previous and the amount to row n, month_current and amount to row n+1, etc.
# The month will save to the DateAnticipated field and the entered amount will save to AnticipatedAmount. Per submit, 14 rows need to be created in the table.
#**************************************************************
class ForecastedCashFlowWidget(MultiWidget):
    def __init__(self, *args, **kwargs):
        super(ForecastedCashFlowWidget, self).__init__(*args, **kwargs)
        
        today = datetime.today()
        start = datetime(today.year, today.month - 1, 1)
        forecast_dates = [start] # initialize with the last month
        # want to include previous month and the next 13
        for i in range(1,14):
            forecast_dates.append(start + relativedelta(months=i))
        
        self.widgets = [NumberInput(forecast) for forecast in forecast_dates]
    
    def decompress(self, value):
        if value:
            return [value]
        return [None for i in range(15)]

class ForecastedCashFlowField(MultiValueField):
    widget = ForecastedCashFlowWidget

    def __init__(self, *args, **kwargs):
        super(ForecastedCashFlowField, self).__init__(*args, **kwargs)
        fields = tuple(CharField() for i in range(1, 15))

    def compress(self, data_list):
        return poop


ProjectFormSet = inlineformset_factory(Saleslead, 
                                       AnticipatedProject, 
                                       fields = ('salesleadid', 
                                                 'cash_flow_responsible', 
                                                 'project_name', 
                                                 'client_name', 
                                                 'subjective_probability', 
                                                 'model_probability')
                                      )
