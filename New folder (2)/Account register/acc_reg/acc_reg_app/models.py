from django.db import models

# Create your models here.

class RegisterForm(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
