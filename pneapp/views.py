from django.shortcuts import render
from .models import Produit

def acceuil(request):
    return render(request, 'acceuil.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def produits_view(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {'produits': produits})
