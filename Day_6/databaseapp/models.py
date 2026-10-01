from django.db import models

class Client(models.Model):
    c_id = models.IntegerField()
    c_name = models.CharField(max_length=100)
    c_company = models.CharField(max_length=100)
    def __str__(self):
        return self.c_name


# Create your models here.
