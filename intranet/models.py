from django.db import models
from django.contrib.auth.models import User

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departements = models.ManyToManyField(Departement, related_name='membres')

    def __str__(self):
        return self.user.username

class Mesage(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='messages')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.auteur.username} - {self.departement.nom} - {self.date_envoi}'
