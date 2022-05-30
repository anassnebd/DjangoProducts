from django.contrib import admin

# Register your models here.
from .models import Produit, Personne, Commande, Categorie


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    pass

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    pass


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    pass

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass
