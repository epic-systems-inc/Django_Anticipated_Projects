from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection
from .DB_models import Saleslead, Company

class AnticipatedProject(models.Model):
    def cursorfetchall():
        cursor = connection.cursor()
        cursor.execute("SELECT secuser.UserID, \
                        NameFirst+' '+NameLast AS Name \
                        FROM \
                        (SELECT UserID, RoleID \
                        FROM security.SecUserRole \
                        WHERE RoleID IN (21, 24, 27)) secrole \
                        INNER JOIN \
                        (SELECT UserID, NameFirst, NameLast \
                        FROM security.SecUser \
                        WHERE Active = 1 AND Token IS NOT NULL) secuser \
                        ON secuser.UserID = secrole.UserID")
        return cursor.fetchall()
    
    CFR_CHOICES = (cursorfetchall())  # cash flow user choices

    aniticipated_proj_id = models.AutoField(db_column="AnticipatedProjectId", primary_key = True)
    date_added = models.DateTimeField(default = timezone.now, db_column='DateAdded')
    sales_lead_id = models.ForeignKey(Saleslead, on_delete = models.DO_NOTHING, db_column='SalesLeadId')
    cash_flow_responsible = models.IntegerField(db_column='CashFlowUserId', choices=CFR_CHOICES)
    company_id = models.ForeignKey(Company, on_delete = models.DO_NOTHING, db_column='CompanyId')
    project_name = models.TextField(max_length = 100, db_column='ProjectName')
    project_alias = models.TextField(max_length = 100, db_column='ProjectAlias', default = project_name)
    subjective_probability = models.IntegerField(db_column='SubjectiveProbability', blank=True, null=True)
    model_probability = models.IntegerField(db_column='CalcProbability')
    forecasted_cash_flow = models.TextField(max_length = 500, db_column='Forecasts', blank=True, null=True) # may need to store this as JSON
    notes = models.TextField(max_length = 400, db_column='Notes', blank=True, null=True)
    archived = models.BooleanField(db_column='Archived', default = 0)

    class Meta:
        managed = True
        db_table = 'AnticipatedProjects'