from django.db import models

# Create your models here.
class Deposit(models.Model):
    amount=models.TimeField(null=False,unique=False)
    txid=models.TextField(null=False,unique=False)