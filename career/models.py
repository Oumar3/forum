from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Avis(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    img = models.FileField(upload_to='media/',null=True,blank=True)
    tdr = models.FileField(upload_to='tdr/',null=True,blank=True)
    body = CKEditor5Field(config_name='extends')
    status = models.CharField(max_length=100, default="Encour")
    date_line = models.CharField(max_length=100)

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    cv =  models.FileField(upload_to='candidats_docs/')
    lettre_de_motivation =  models.FileField(upload_to='candidats_docs/')
    experience_professionnelle = models.CharField(max_length=100)
    niveau_d_etude = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"