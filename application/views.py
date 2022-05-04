from .form import LivreForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'application/index.html')

def main(request):
    return render(request, 'main.html')

def formulaire(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
                return HttpResponseRedirect("application/affichage")
        else:
                return render(request, 'application/formulaire.html', {'form': form})
    else:
            form = LivreForm()
            return render(request, 'application/formulaire.html', {'form': form})


def traitement(request):
    pForm = LivreForm(request.POST)
    if pForm.is_valid():
        livre = pForm.save()
        return render(request, 'application/affichage.html' , {'livre' : livre})
    else:
        return render(request, 'application/formulaire.html', {'form': pForm})
    
def affichage(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"application/affichage.html",{"livre": livre})

def affichetout(request):
    livre = models.Livre.objects.all()
    return render(request, 'application/affichetout.html', {"livre": livre})


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"/application/affichage.html",{"livre" : livre})
        else:
            return render(request,"application/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"application/ajout.html",{"form" : form})
    
    
def update(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id; # modification de l'id de l'objet
        livre.save() # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect("application/")
    else:
        return render(request, "application/update.html", {"form": lform, "id": id})