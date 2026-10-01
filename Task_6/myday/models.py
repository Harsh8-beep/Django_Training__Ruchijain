from django.db import models

class Product(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=100)
    p_price = models.FloatField()
    p_offer = models.FloatField()
    def __str__(self):
        return self.p_name

# Create your models here.
