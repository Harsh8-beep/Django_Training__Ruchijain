from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    cgpa = models.FloatField(null=True, blank=True)
    iq = models.IntegerField(null=True, blank=True)
    profile_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
      
# Create your models here.
