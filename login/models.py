from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Login(models.Model):
    email=models.EmailField(unique=True,null=False)
    password=models.TextField(unique=True,null=False)
    balance=models.TextField(default="0.00")

