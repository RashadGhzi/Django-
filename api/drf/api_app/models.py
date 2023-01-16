from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    date = models.DateField()

 