from pyexpat.errors import messages
from turtle import back
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from engins.models import Engins
from equipements.models import Materiel
from gestions.models import Employer, Mission, Projet
from parametres.forms import FonctionForm, Type_materialForm, Type_vehiculeForm

from parametres.models import Fonction, Type_materiel, Type_vehicule
from django.contrib import messages
from django.template.loader import get_template, render_to_string
from django.template.context_processors import csrf
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='compteuser:login')
def index(request):
    today = datetime.date.today()
    missions = Mission.objects.filter(etat_mission = "EN COURS").order_by('-id')[:10]
    engins = Engins.objects.filter(etat = "DISPONIBLE")

    nb_mission_en_cours = len(Mission.objects.filter(etat_mission = "EN COURS"))
    nb_vehicule_disponible = len(Engins.objects.filter(etat = "DISPONIBLE") & Engins.objects.filter(type_engins = 2))
    nb_moto_disponible = len(Engins.objects.filter(etat = "DISPONIBLE") & Engins.objects.filter(type_engins = 1)) + len(Engins.objects.filter(etat = "DISPONIBLE") & Engins.objects.filter(type_engins = 3))
    nb_voiture_garage = len(Engins.objects.filter(etat = "OCCUPE") & Engins.objects.filter(type_engins = 2))
    nb_moto_garage = len(Engins.objects.filter(etat = "OCCUPE") & Engins.objects.filter(type_engins = 1))
    nb_tois_roue_garage = len(Engins.objects.filter(etat = "OCCUPE") & Engins.objects.filter(type_engins = 3) )
    nb_employe_activite = len(Employer.objects.filter(etat = "EN ACTIVITE")) + len(Employer.objects.filter(etat = "OCCUPE"))
    nb_projet_en_cours = len(Projet.objects.filter(etat = "EN COURS"))
    nb_equipement_gps_fonctionnelle = len(Materiel.objects.filter(etat = "FONCTIONNELLE") & Materiel.objects.filter(type_materiel = 2)) + len(Materiel.objects.filter(etat = "ATTRIBUER") & Materiel.objects.filter(type_materiel = 2))
    nb_equipement_ordi_fonctionnelle = len(Materiel.objects.filter(etat = "FONCTIONNELLE") & Materiel.objects.filter(type_materiel = 1)) + len(Materiel.objects.filter(etat = "ATTRIBUER") & Materiel.objects.filter(type_materiel = 1))
    
    context = {
        'missions': missions,
        'engins': engins,
        'nb_mission_en_cours':nb_mission_en_cours,
        'nb_vehicule_disponible':nb_vehicule_disponible,
        'nb_moto_disponible':nb_moto_disponible,
        'nb_voiture_garage':nb_voiture_garage,
        'nb_moto_garage':nb_moto_garage,
        'nb_tois_roue_garage':nb_tois_roue_garage,
        'nb_employe_activite':nb_employe_activite,
        'nb_projet_en_cours':nb_projet_en_cours,
        'nb_equipement_gps_fonctionnelle':nb_equipement_gps_fonctionnelle,
        "today":today,
        "nb_equipement_ordi_fonctionnelle":nb_equipement_ordi_fonctionnelle
    }
    return render(request, 'pages/home.html', context)
   
@login_required(login_url='compteuser:login')
def fonctionhomne(request):
    fonctions = Fonction.objects.all()
    form = FonctionForm()
    error = ''
    if request.method == 'POST':
        forms = FonctionForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Enregistrement effectué avec succèss !')
        else:
            error = 'Attention ! Champs vide ou libelle exite déja'
            messages.error(request, 'Attention ! Champs vide ou libelle exite déja')
            
    context = {
        'fonctions':fonctions,
        'form':form,
        'error':error
    }
    
    return render(request,'fonction.html',context)

@login_required(login_url='compteuser:login')
def typeMaterialhomne(request):
    tymateriels = Type_materiel.objects.all()
    form = Type_materialForm()
    error = ''
    if request.method == 'POST':
        forms = Type_materialForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Enregistrement effectué avec succèss !')
        else:
            error = 'Attention ! Champs vide ou libelle exite déja'
            messages.error(request, 'Attention ! Champs vide ou libelle exite déja')
            
    context = {
        'tymateriels':tymateriels,
        'form':form,
        'error':error
    }
    return render(request,'tymaterial.html',context)

@login_required(login_url='compteuser:login')
def typeVehiculehomne(request):
    tyvehicules = Type_vehicule.objects.all()
    form = Type_vehiculeForm()
    error = ''
    if request.method == 'POST':
        forms = Type_vehiculeForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Enregistrement effectué avec succèss !')
        else:
            error = 'Attention ! Champs vide ou libelle exite déja'
            messages.error(request, 'Attention ! Champs vide ou libelle exite déja')
    
    context = {
        'tyvehicules':tyvehicules,
        'form':form,
        'error':error
    }
    return render(request,'tyvehicule.html',context)



@login_required(login_url='compteuser:login')
def delFonction(request, id= None):
    fonction = Fonction.objects.get(id=id)
    fonction.delete()
    messages.success(request, "Lélément "+fonction.libelle+" a été supprimé avec succès")
    return HttpResponseRedirect(reverse('parametres:fonction'))


@login_required(login_url='compteuser:login')
def upFonction(request, id= None):
    fonction = Fonction.objects.get(id=id)
    form = FonctionForm(request.POST or None, request.FILES or None, instance=fonction)
    context = {
        'fonction':fonction,
        'form':form
    }
    context.update(csrf(request))
    templateStr = render_to_string("modal/edit_fonction.html", context)
    return JsonResponse({'templateStr':templateStr,'id':id},safe=False)



@login_required(login_url='compteuser:login')
def updateFonction(request):
    id = request.POST['fonct']
    fonction = Fonction.objects.get(id=int(id))
    fonction.libelle = request.POST['libelle']
    fonction.save()
    messages.success(request, "Lélément "+fonction.libelle+" a été modifié avec succès")
    return HttpResponseRedirect(reverse('parametres:fonction'))



@login_required(login_url='compteuser:login')
def delTymateriel(request,id=None):
    tymateriel = Type_materiel.objects.get(id=id)
    tymateriel.delete()
    messages.success(request, "Lélément "+tymateriel.libelle+" a été supprimé avec succès")
    return HttpResponseRedirect(reverse('parametres:typem'))
    
 
 
@login_required(login_url='compteuser:login')   
def upTymateriel(request, id= None):
    tymateriel = Type_materiel.objects.get(id=id)
    form = Type_materialForm(request.POST or None, request.FILES or None, instance=tymateriel)
    context = {
        'tymateriel':tymateriel,
        'form':form
    }
    context.update(csrf(request))
    templateStr = render_to_string("modal/edit_tymateriel.html", context)
    return JsonResponse({'templateStr':templateStr,'id':id},safe=False)




@login_required(login_url='compteuser:login')
def updateTymateriel(request):
    id = request.POST['tymateriel']
    tymateriel = Type_materiel.objects.get(id=int(id))
    tymateriel.libelle = request.POST['libelle']
    tymateriel.save()
    messages.success(request, "Lélément "+tymateriel.libelle+" a été modifié avec succès")
    return HttpResponseRedirect(reverse('parametres:typem'))


@login_required(login_url='compteuser:login')
def delVehicule(request,id=None):
    vehicule = Type_vehicule.objects.get(id=id)
    vehicule.delete()
    messages.success(request, "Lélément "+vehicule.libelle+" a été supprimé avec succès")
    return HttpResponseRedirect(reverse('parametres:tyvehicule'))


@login_required(login_url='compteuser:login')
def upVehicule(request, id= None):
    vehicule = Type_vehicule.objects.get(id=id)
    form = Type_vehiculeForm(request.POST or None, request.FILES or None, instance=vehicule)
    context = {
        'vehicule':vehicule,
        'form':form
    }
    context.update(csrf(request))
    templateStr = render_to_string("modal/edit_vehicule.html", context)
    return JsonResponse({'templateStr':templateStr,'id':id},safe=False)



@login_required(login_url='compteuser:login')
def updateVehicule(request):
    id = request.POST['vehicule']
    vehicule = Type_vehicule.objects.get(id=int(id))
    vehicule.libelle = request.POST['libelle']
    vehicule.save()
    messages.success(request, "Lélément "+vehicule.libelle+" a été modifié avec succès")
    return HttpResponseRedirect(reverse('parametres:tyvehicule'))







######-------------------------------------------------------MPI----------------------------01/08/2022-------------------------------------------------


