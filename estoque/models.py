from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)