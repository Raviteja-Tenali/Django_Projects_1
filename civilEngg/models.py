from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=1000)
    qualification = models.CharField(max_length=1000)
    passedout   = models.IntegerField()
    city = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=1000)