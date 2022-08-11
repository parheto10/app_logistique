from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from engins.forms import EnginsForm

from engins.models import Engins
from parametres.models import Type_vehicule
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='compteuser:login')
def home(request):
    engins = Engins.objects.all()
    
    context = {
        'engins':engins
    }
    return render(request,'home.html',context)

@login_required(login_url='compteuser:login')
def AjoutCarView(request):
    typevehicules = Type_vehicule.objects.all()
    form = EnginsForm()
    
    if request.method == 'POST':
        forms = EnginsForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Enregistrement effectué avec succèss !")
            return HttpResponseRedirect(reverse('engins:home'))
    
    context = {
        'typevehicules':typevehicules,
        'form':form
    }
    
    return render(request, 'ajoutpage.html',context)


@login_required(login_url='compteuser:login')
def EditCarView(request,id=None):
    engin = Engins.objects.get(id=id)
    form = EnginsForm(request.POST or None, request.FILES or None, instance=engin)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Mise à jour effectué avec succèss !")
            
    context = {
        'form':form,
        'engin':engin
    }
    
    return render(request, 'editpage.html',context)


@login_required(login_url='compteuser:login')
def DeleteCars(request, id=None):
    engin = Engins.objects.get(id=id)
    engin.delete()
    messages.success(request, "Suppression effectué avec succèss !")
    return HttpResponseRedirect(reverse('engins:home'))
        
    
    