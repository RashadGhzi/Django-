from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.PositiveBigIntegerField()
    register=models.PositiveBigIntegerField() 
    address=models.TextField() 



    def __str__(self):
        return self.name 
    