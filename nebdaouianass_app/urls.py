from django.urls import path
from . import views


urlpatterns = [
    path('produit/', views.index),
    path('produit/search/', views.search),
    path('produit/detaille/<int:id>', views.detaille),
    path('personne/', views.personne),
    path('commande/<int:id>', views.commande),
    path('produit/create/', views.get_produit),
    path('categorie/create/', views.get_categorie),
    path('personne/create/', views.get_personne),
    path('commande/create/', views.get_commande),

]
