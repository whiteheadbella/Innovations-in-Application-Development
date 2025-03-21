# chatbot/models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Securely hash it before saving
    position = models.CharField(max_length=50)
    hired = models.DateField()

    def __str__(self):
        return self.name
