from .forms import LivreForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'application/index.html')



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


def affichage(request):
    pForm = LivreForm(request.POST)
    if pForm.is_valid():
        livre = pForm.save()
        return render(request, 'application/affichage.html' , {'livre' : livre})
    else:
        return render(request, 'application/formulaire.html', {'form': pForm})