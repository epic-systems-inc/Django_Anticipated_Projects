from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Saleslead, AnticipatedProject
from datetime import datetime, timedelta
from dateutil.relativedelta import *

# Create your views here.
def home(request):
    #context = {
    #    "posts": Post.objects.all()
    #}
    return render(request, "dashboard/home.html")

class ProjectListView(ListView):
    model = AnticipatedProject
    template_name = 'dashboard/home.html'
    context_object_name = 'projects'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.today()
        start = datetime(today.year, today.month - 1, 1)
        forecast_dates = [start] # initialize with the last month
        # want to include the next 17 months in the view
        for i in range(1,18):
            forecast_dates.append(start + relativedelta(months=i))
        
        context["forecast_dates"] = forecast_dates

        return context



