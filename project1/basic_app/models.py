from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    date = models.DateField()   
