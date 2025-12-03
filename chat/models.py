# models.py
from django.db import models
from signup.models import Signup

class Message(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    content = models.TextField()
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
