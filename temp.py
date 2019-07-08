from dashboard.models import AnticipatedProject, Saleslead, Company
import json
import random

with open('projects.json') as f:
    projects_json = json.load(f)

for project in projects_json:
    project = AnticipatedProject(sales_lead_id=Saleslead.objects.get(salesleadid=random.randint(1000, 1200)),
    cash_flow_responsible = project['cash_flow_responsible'], company_id=Company.objects.get(companyid=random.randint(100, 600)), 
    project_name=project['project_name'], subjective_probability=project['subjective_probability'],
    model_probability=project['model_probability'],forecasted_cash_flow=project['forecasted_cash_flow'], 
    notes=project['notes'], archived=project['archived'])
    project.save()