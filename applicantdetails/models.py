from django.db import models

# Create your models here.
class applicantdetails(models.Model):
    japplient_app_id = models.IntegerField(primary_key=True)
    japplient_results = models.CharField(max_length=50)
    japplient_passyear = models.IntegerField()
    japplient_qualification = models.CharField(max_length=50)
    japplient_languageflu = models.CharField(max_length=20)
    japplient_status = models.CharField(max_length=20)
    japplient_cv = models.CharField(max_length=50)
    japplient_applicant = models.CharField(max_length=50)