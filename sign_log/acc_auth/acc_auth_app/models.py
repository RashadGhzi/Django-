from django.db import models

# Create your models here.
class Authentication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    retype_password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
