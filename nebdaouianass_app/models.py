from django.db import models

# Create your models here.


class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=30)

    def __str__(self):
        return self.nomCategorie


class Produit(models.Model):
    produitRef = models.CharField(max_length=30)
    nomProduit = models.CharField(max_length=30)
    dateProduction = models.DateField()
    prix = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nomProduit



class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    referenceCmd = models.CharField(max_length=30)
    dateCmd = models.DateField()
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.referenceCmd

