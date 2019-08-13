from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection
from .DB_models import Salesleadquote, Company, Quotestatus

class AnticipatedProject(Salesleadquote):
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
    
    CFR_CHOICES = tuple(cursorfetchall())  # cash flow user choices

    aniticipated_proj_id = models.AutoField(db_column="AnticipatedProjectId", primary_key = True)
    #sales_lead_quote_id = models.OneToOneField(Salesleadquote, on_delete = models.DO_NOTHING, db_column='SalesLeadQuoteId', primary_key=True)
    cash_flow_responsible = models.IntegerField(db_column='CashFlowUserId', choices=CFR_CHOICES)
    subjective_probability = models.IntegerField(db_column='SubjectiveProbability', blank=True, null=True)
    notes = models.TextField(max_length = 400, db_column='Notes', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AnticipatedProjects'
