from django.db import models

class Personne(models.Model):
    OPTIONS = (
        ('masculin', 'masculin'),
        ('feminin', 'feminin'),
    )
    id_personne = models.AutoField(primary_key=True,auto_created=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=OPTIONS)
