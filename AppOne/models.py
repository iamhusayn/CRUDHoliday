from django.db import models

# Create your models here.
class AddBooks(models.Model):
    Tittle = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    Field = models.CharField(max_length=100)
    Status = models.BooleanField(default=False)
    Published = models.DateField
    Rating = models.Choices