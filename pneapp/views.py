from django.shortcuts import render
from .models import Produit

def acceuil(request):
    return render(request, 'acceuil.html')

def produits_view(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {'produits': produits})
