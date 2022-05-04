from .form import LivreForm
from .models import dico
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'application/index.html')


def main(request):
    return render(request, 'main.html')


def traitement(request):
    pForm = LivreForm(request.POST)
    if pForm.is_valid():
        livre = pForm.save()
        return render(request, 'application/affichage.html', {'livre': livre})
    else:
        return render(request, 'application/formulaire.html', {'form': pForm})


def affichage(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "application/affichage.html", {"livre": livre})


def affichetout(request):
    livre = models.Livre.objects.all()
    return render(request, 'application/affichetout.html', {"livre": livre})


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():  # validation du formulaire.
            livre = form.save()  # sauvegarde dans la base
            return render(request, "/application/affichage.html", {"livre": livre})
        else:
            return render(request, "application/ajout.html", {"form": form})
    else:
        form = LivreForm()  # création d'un formulaire vide
        return render(request, "application/ajout.html", {"form": form})



def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    form = LivreForm(livre.dico())
    return render(request, "application/ajout.html", {"form": form, "id":id})

def updatetraitement(request, id):
    pForm = LivreForm(request.POST)
    if pForm.is_valid():
        Livre = pForm.save(commit=False)
        Livre.id = id
        Livre.save()
        return render(request, 'application/affichage.html', {'Livre': Livre})
    else:
        return render(request, 'application/formulaire.html', {'form': pForm})
