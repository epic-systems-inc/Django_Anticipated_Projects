from django.forms import inlineformset_factory, MultiWidget, MultiValueField, NumberInput, CharField
from .models import AnticipatedProject, Saleslead
from datetime import datetime, timedelta
from dateutil.relativedelta import *

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
