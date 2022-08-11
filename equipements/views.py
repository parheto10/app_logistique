from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from equipements.forms import AccessoireForm, MaterielsForm
from django.contrib import messages
from django.template.context_processors import csrf
from django.template.loader import get_template, render_to_string

from equipements.models import Accessoire, Materiel
from gestions.forms import AttributionForm
from gestions.models import Attribution, Employer
from parametres.models import Type_materiel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='compteuser:login')
def AccessoiresView(request):
    accessoires = Accessoire.objects.all()
    form = AccessoireForm()
    error = ''
    if request.method == 'POST':
        forms = AccessoireForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Enregistrement effectué avec succèss !')
        else:
            error = 'Attention ! Champs vide ou libelle exite déja'
            messages.error(request, 'Attention ! Champs vide ou libelle exite déja')
        
            
    context = {
        'accessoires':accessoires,
        'form':form,
        'error':error
    }
    
    return render(request, 'accessoires.html',context) 


@login_required(login_url='compteuser:login')
def Edit_accessoires(request,id =None):
    accessoire = Accessoire.objects.get(id= id)
    form = AccessoireForm(request.POST or None, request.FILES or None, instance=accessoire)
    context = {
        'accessoire':accessoire,
        'form':form
    }
    context.update(csrf(request))
    templateStr = render_to_string("modal/edit_accessoire.html", context)
    return JsonResponse({'templateStr':templateStr,'id':id},safe=False)

@login_required(login_url='compteuser:login')
def Update_accessoire(request):
    id = request.POST['accessoire']
    accessoire = Accessoire.objects.get(id = int(id))
    form = AccessoireForm(request.POST or None, request.FILES or None, instance=accessoire)
    form.save()
    messages.success(request, "Lélément "+accessoire.libelle+" a été modifié avec succès")
    return HttpResponseRedirect(reverse('equipements:accesooires'))
  
    
@login_required(login_url='compteuser:login')   
def Delete_accessoire(request, id = None):
    accessoire = Accessoire.objects.get(id= id)
    accessoire.delete()
    messages.success(request, "Lélément "+accessoire.libelle+" a été supprimé avec succès")
    return HttpResponseRedirect(reverse('equipements:accesooires'))


@login_required(login_url='compteuser:login')
def MaterielView(request):
    equipements = Materiel.objects.all()
    
    context = {
        'equipements':equipements
    }
    return render(request, 'materiels.html',context) 


@login_required(login_url='compteuser:login')
def Ajout_equipement(request):
    type_materiels = Type_materiel.objects.all()
    form = MaterielsForm()
    
    if request.method == 'POST':
        forms = MaterielsForm(request.POST, request.FILES)
        forms.save()
        messages.success(request, "Enregistrement effectué avec succèss !")
        return HttpResponseRedirect(reverse('equipements:materiels'))
    
    
    context = {
        'type_materiels':type_materiels,
        'form':form
    }
    
    return render(request, 'ajoutmateriel.html',context)


@login_required(login_url='compteuser:login')
def Edit_equipement(request,id= None):
    equipement = Materiel.objects.get(id= id)

        
    form = MaterielsForm(request.POST or None, request.FILES or None, instance=equipement)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Mise à jour effectué avec succèss !")
          
          
    try :        
        attribut = Attribution.objects.filter(materiel_id = id).latest('id')
        context = {
            'form':form,
            'equipement':equipement,
            'user':attribut
        }
    except Attribution.DoesNotExist :  
        context = {
            'form':form,
            'equipement':equipement,
            # 'user':attribut
        }
    
    return render(request, 'editmateriel.html',context)


@login_required(login_url='compteuser:login')
def DeleteMateriels(request, id= None):
    equipement = Materiel.objects.get(id= id)
    equipement.delete()
    messages.success(request, "Suppression effectué avec succèss !")
    return HttpResponseRedirect(reverse('equipements:materiels'))


@login_required(login_url='compteuser:login')
def Attribut_Equipement(request, id= None):
    employe = Employer.objects.filter(etat = 'EN ACTIVITE') | Employer.objects.filter(etat = 'OCCUPE')
    materiel = Materiel.objects.get(id = id)
    form = AttributionForm()
    context = {
        'materiel':materiel,
        'employes':employe,
        'form':form
    }
    context.update(csrf(request))
    templateStr = render_to_string("modal/att_form_view.html", context)
    return JsonResponse({'templateStr':templateStr,'id':id},safe=False)


@login_required(login_url='compteuser:login')
def Store_attribution(request):
    materiel = Materiel.objects.get(id = int(request.POST['equipement']))
    employe = Employer.objects.get(id= int(request.POST['employe']))
    if request.method == 'POST':
        if request.POST['date_attribution'] != '':
            attribution = Attribution()
            attribution.date_attribution = request.POST['date_attribution']
            attribution.employe_id = employe.id
            attribution.materiel_id = materiel.id
            attribution.save()
            materiel.etat = "ATTRIBUER"
            materiel.save()
            messages.success(request, "Attribution du materiel "+materiel.marque+ " a Mr "+employe.nom+"")
            return HttpResponseRedirect(reverse('equipements:materiels'))
        else:
            messages.success(request, "Un problème est subvenu lors de l'attribution réessayez.")
            return HttpResponseRedirect(reverse('equipements:materiels'))
        

@login_required(login_url='compteuser:login')
def Restitu_equipement(request, id=None):
    try:
        rendre = Attribution.objects.filter(materiel_id = id).latest('id')
        materiel = Materiel.objects.get(id = id)
        rendre.etat = True
        rendre.save()
        materiel.etat = "FONCTIONNELLE"
        materiel.save()
        
    except Attribution.DoesNotExist :
       pass 
            