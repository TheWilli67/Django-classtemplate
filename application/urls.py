from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('affichage/', views.affichage),
    path('affichetout/', views.affichetout),
    path('main/', views.main),
    path('traitement/', views.traitement),
    path('ajout/', views.ajout),
    path('affichage/<int:id>/',views.affichage),
    path('update/<int:id>/',views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete)
]