from django.db import models

# Create your models here.

class dbModel(models.Model):
    db = models.FileField(upload_to="db")
    title = models.CharField(max_length=200)
    