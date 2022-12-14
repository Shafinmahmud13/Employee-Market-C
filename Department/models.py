from django.db import models

# Create your models here.
class Department(models.Model):
    Department_name = models.CharField(max_length=10)
    Department_id = models.IntegerField(primary_key=True)
