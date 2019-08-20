from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView
from .models import Salesleadquote
from dashboard.forms import AnticipatedAwardForm
from datetime import datetime, timedelta
from dateutil.relativedelta import *

class ProjectListView(ListView):
    model = Salesleadquote
    template_name = 'dashboard/home.html'
    context_object_name = 'anticipated_projects'
    ordering = ['-createddate']

    def get_queryset(self):
        return Salesleadquote.pivoted_objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.today()
        start = datetime(today.year, today.month - 1, 1)
        rolling_fourteen_months = [start] # initialize with the last month
        # want to include previous month, this month, and the next 12 in the view
        for i in range(1,13):
            rolling_fourteen_months.append(start + relativedelta(months=i))
        
        context["rolling_fourteen_months"] = [date.strftime("%Y-%m-%d") for date in rolling_fourteen_months]
        return context

def save_project_form(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = Salesleadquote.pivoted_objects.all()
            data['html_projects_list'] = render_to_string('dashboard/partial_project_list.html',
                                                         {'anticipated_projects': projects})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def project_update(request, pk):
    project = get_object_or_404(Salesleadquote, pk=pk)
    if request.method == "POST":
        form = AnticipatedAwardForm(request.POST, instance=project)
    else:
        form = AnticipatedAwardForm(instance=project)
    return save_project_form(request, form, 'dashboard/partial_project_update.html')