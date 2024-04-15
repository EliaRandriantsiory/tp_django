from django.db import models
from Personne.models import Personne

# from fiara.Personne.models import models

class Voiture(models.Model):
    id_voiture = models.IntegerField(primary_key=True,auto_created=True )
    num_matricule = models.CharField(max_length=10)
    marque = models.CharField(max_length=10)
    image = models.CharField(max_length=1000)
    id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)

