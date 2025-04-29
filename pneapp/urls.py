# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
        path('produits/', views.produits_view, name='produits'),

]
