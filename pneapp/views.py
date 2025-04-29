from django.shortcuts import render
from .models import Produit

def base(request):
    return render(request, 'base.html')

def produits_view(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {'produits': produits})
