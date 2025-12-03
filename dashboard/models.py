from django.db import models

# Create your models here.
class Balance(models.Model):
    balance=models.TextField(default=0.0)