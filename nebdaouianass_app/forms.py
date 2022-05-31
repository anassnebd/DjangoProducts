from django import forms
from .models import Categorie

class ProduitForm(forms.Form):
    produitRef = forms.CharField(label='Produit Reference', max_length=100)
    nomProduit = forms.CharField(label='nom de produit', max_length=100)
    dateProduction = forms.CharField(label='date production', max_length=100)
    prix = forms.FloatField(label='Prix')
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

class CategorieForm(forms.Form):

    nomCategorie = forms.CharField(label='nom categorie', max_length=100)

class PersonneForm(forms.Form):

    nom = forms.CharField(label='Nom', max_length=100)
    prenom = forms.CharField(label='Prenom', max_length=100)
    email = forms.CharField(label='email', max_length=100)
