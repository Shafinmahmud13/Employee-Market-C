from django.db import models

# Create your models here
class japplient(models.Model):
     japplient_id = models.IntegerField(primary_key=True)
     japplient_edu = models.CharField(max_length=50)
     japplient_mobile= models.IntegerField()
     japplient_user=models.IntegerField()
