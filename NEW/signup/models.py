from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)  # store hashed password only
    balance=models.TextField(default="0.00")

    def __str__(self):
        return self.email
