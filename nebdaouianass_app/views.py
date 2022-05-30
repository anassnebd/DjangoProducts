from django.shortcuts import render

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import context
from .models import Categorie, Produit , Personne, Commande
from .forms import ProduitForm, CategorieForm, PersonneForm


def index(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'produits': page_obj}
    return render(request, 'base.html', context)

def detaille(request, id):
    try:
        produit = Produit.objects.get(id=id)
        context = {'produit': produit}
    except Produit.DoesNotExist:
        return redirect('/Produit')
    return render(request, 'detaille.html', context)
#add to detaille


def search(request):
    filteredProduits = Produit.objects.filter(nomProduit__icontains=request.GET.get("search", ""))
    paginator = Paginator(filteredProduits, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'produits': page_obj}
    return render(request, "base.html", context)


def personne(request):
    personnes = Personne.objects.all()
    paginator = Paginator(personnes, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'personnes': page_obj}
    return render(request, 'personne.html', context)


def commande(request, id):
    personn =Personne.objects.get(id=id)
    commandes = Commande.objects.filter(personne=personn)
    paginator = Paginator(commandes, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'commandes': page_obj}
    return render(request, 'commande.html', context)

def get_produit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProduitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            produitRef=request.POST.get("produitRef", "")
            nomProduit=request.POST.get("nomProduit", "")
            dateProduction=request.POST.get("dateProduction",  "")
            prix=request.POST.get("prix", "")
            categori=request.POST.get("categorie", "")
            categori=Categorie.objects.get(id=categori)
            produit=Produit.objects.create(produitRef=produitRef,nomProduit=nomProduit,dateProduction=dateProduction,prix=prix,categorie=categori)
            produit.save()


            # redirect to a new URL:
            return HttpResponseRedirect('/produit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProduitForm()

    return render(request, 'produitForm.html', {'form': form})

def get_categorie(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategorieForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nomCategorie= request.POST.get("nomCategorie", "")
            categorie=Categorie.objects.create(nomCategorie=nomCategorie)
            categorie.save()


            # redirect to a new URL:
            return HttpResponseRedirect('/produit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategorieForm()

    return render(request, 'categorieForm.html', {'form': form})

def get_personne(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonneForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nom = request.POST.get("nom", "")
            prenom = request.POST.get("prenom", "")
            email = request.POST.get("email", "")
            personne=Personne.objects.create(nom=nom, prenom=prenom, email=email)
            personne.save()


            # redirect to a new URL:
            return HttpResponseRedirect('/produit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonneForm()

    return render(request, 'personneForm.html', {'form': form})

def get_commande(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProduitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            referenceCmd= request.POST.get("referenceCmd", "")
            dateCmd = request.POST.get("dateCmd", "")
            personn = request.POST.get("personne", "")
            personne = Personne.objects.get(nom=personn)
            produit = request.POST.get("produit", "")
            personne=Produit.objects.create(referenceCmd=referenceCmd,dateCmd=dateCmd,personne=personne,produit=produit)
            personne.save()


            # redirect to a new URL:
            return HttpResponseRedirect('produit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonneForm()

    return render(request, 'commandeForm.html', {'form': form})
