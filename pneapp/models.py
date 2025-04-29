from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='produits/')

    def __str__(self):
        return self.nom
