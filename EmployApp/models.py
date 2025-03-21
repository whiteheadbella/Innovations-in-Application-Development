from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=60, null=True)
    password = models.CharField(max_length=25, null=True)
    position = models.CharField(max_length=50, null=True)  # Ensure this exists
    hired = models.DateField(null=True, blank=True)  # Ensure this exists

    def __str__(self):
        return self.name