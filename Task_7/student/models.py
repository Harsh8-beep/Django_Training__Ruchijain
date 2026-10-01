from django.db import models


class student(models.Model):
    stuname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.stuname

# Create your models here.
