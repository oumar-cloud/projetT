# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
        path('produits/', views.produits_view, name='produits'),

]
