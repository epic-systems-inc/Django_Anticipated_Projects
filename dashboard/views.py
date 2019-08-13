from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import AnticipatedProject, Salesleadquote
from dashboard.forms import AnticipatedAwardForm
from datetime import datetime, timedelta
from dateutil.relativedelta import *

# Create your views here.
def home(request):
    #context = {
    #    "projects": AnticipatedProjects.objects.all()
    #}
    return render(request, "dashboard/home.html")


class ProjectListView(ListView):
    queryset = Salesleadquote.rolling_fourteen_months_objects.my_custom_sql()
    template_name = 'dashboard/home.html'
    context_object_name = 'anticipated_projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.today()
        start = datetime(today.year, today.month - 1, 1)
        rolling_fourteen_months = [start] # initialize with the last month
        # want to include previous month, this month, and the next 12 in the view
        for i in range(1,13):
            rolling_fourteen_months.append(start + relativedelta(months=i))
        
        context["rolling_fourteen_months"] = [date.strftime("%Y-%m-%d") for date in rolling_fourteen_months]
        context["keys"] = self.queryset[0].keys()
        return context



