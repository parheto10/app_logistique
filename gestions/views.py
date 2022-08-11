from ast import Str
import datetime
from django.contrib.staticfiles import finders
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from engins.models import Engins
from gestions.forms import CourseForm, EmployeForm, ProjetForm
from django.contrib import messages
from xhtml2pdf import pisa

from gestions.models import Course, Employer, Mission, Projet
from django.template.loader import get_template, render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='compteuser:login')
def EmployeView(request):
    employes = Employer.objects.all()
    
    context = {
        'employes':employes
    }
    return render(request, 'empl/employe.html',context)

@login_required(login_url='compteuser:login')
def Ajout_employe(request):
    form = EmployeForm()
    if request.method == 'POST':
        forms = EmployeForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Enregistrement effectué avec succèss !")
            return HttpResponseRedirect(reverse('gestions:employes'))
        else :
            messages.error(request, 'Attention ! Champs vide ou Matricule exite déja')
    
    context = {
        'form':form
    }
    
    return render(request, 'empl/ajout_emp.html',context)


@login_required(login_url='compteuser:login')
def Edit_employe(request, id= None):
    employe = Employer.objects.get(id= id)
    form = EmployeForm(request.POST or None, request.FILES or None, instance=employe)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Mise à jour effectué avec succèss !")
            return HttpResponseRedirect(reverse('gestions:employes'))
            
    context = {
        'form':form,
        'employe':employe
    }
    
    return render(request, 'empl/edit_emp.html',context)



@login_required(login_url='compteuser:login')
def ProjetView(request):
    projets = Projet.objects.all()
    
    context = {
        'projets':projets
    }
    
    return render(request, 'proj/projet.html',context)


@login_required(login_url='compteuser:login')
def Ajout_projet(request):
    form = ProjetForm()
    if request.method == 'POST':
        forms = ProjetForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Enregistrement effectué avec succèss !")
            return HttpResponseRedirect(reverse('gestions:projets'))
    
    context = {
        'form':form
    }
    
    return render(request, 'proj/ajout_proj.html',context)



@login_required(login_url='compteuser:login')
def Edit_projet(request, id =None):
    projet = Projet.objects.get(id=id)
    form = ProjetForm(request.POST or None, request.FILES or None, instance=projet)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Mise à jour effectué avec succèss !")
          
    
    context = {
        'form':form,
        'projet':projet
    }
    return render(request, 'proj/edit_proj.html',context)



@login_required(login_url='compteuser:login')
def CoursesView(request):
    courses = Course.objects.order_by('-id')
    
    for course in courses :
        # print(course.id)
        time = datetime.datetime.now()
        if course.created_at.day == time.day:
            reduct = time.hour - course.created_at.hour
            if reduct >= 1 :
                course.diff = str(time.hour - course.created_at.hour) + " heurs"
            else :
                course.diff = "Moins d'une heure"
        else:
            if course.created_at.month == time.month:
                course.diff = str(time.day - course.created_at.day) + " jours"
            else:
                if course.created_at.year == time.year:
                    course.diff = str(time.month - course.created_at.month) + " mois"
                    
    context = {
        'courses':courses
    }
    
    return render(request, 'course/index.html',context)



@login_required(login_url='compteuser:login')
def Ajout_course(request):
    vehicules = Engins.objects.filter(etat = 'DISPONIBLE')
    employes = Employer.objects.filter(etat = 'EN ACTIVITE')
    
    if request.method == 'POST':
        course = Course()
        course.depart = request.POST['depart']
        course.destination = request.POST['destination']
        course.date_course = request.POST['date_course']
        course.etat_course = request.POST['etat_course']
        course.motif = request.POST['motif']
        course.employe_id = int(request.POST['employe'])
        course.vehicule_id = int(request.POST['vehicule'])
        course.save()
        
        engin = Engins.objects.get(id = course.vehicule.id)
        engin.etat = 'OCCUPE'
        engin.save()
        
        user = Employer.objects.get(id = course.employe.id)
        user.etat = 'OCCUPE'
        user.save()
        
        messages.success(request, "Enregistrement effectué avec succèss !")
        return HttpResponseRedirect(reverse('gestions:courses'))
        
    context = {
        'vehicules':vehicules,
        'employes':employes,
    }
    
    return render(request, 'course/ajout_course.html',context)



@login_required(login_url='compteuser:login')
def Edit_course(request,id =None):
    course = Course.objects.get(id= id)
    
    context = {
        'course':course
    }
    
    return render(request, 'course/edit_course.html',context)


@login_required(login_url='compteuser:login')
def Delete_course(request, id=None):
    course = Course.objects.get(id=id)
    
    engin = Engins.objects.get(id = course.vehicule.id)
    engin.etat = 'DISPONIBLE'
    engin.save()
    
    user = Employer.objects.get(id = course.employe.id)
    user.etat = 'EN ACTIVITE'
    user.save()
    
    course.delete()
    messages.success(request, "Suppression effectué avec succèss !")
    return HttpResponseRedirect(reverse('gestions:courses'))



@login_required(login_url='compteuser:login')
def Termine_course(request,id = None):
    course = Course.objects.get(id=id)
    course.etat_course = 'TERMINER'
    course.date_fin = datetime.datetime.now()
    course.save()
    
    engin = Engins.objects.get(id = course.vehicule.id)
    engin.etat = 'DISPONIBLE'
    engin.save()
    
    user = Employer.objects.get(id = course.employe.id)
    user.etat = 'EN ACTIVITE'
    user.save()
    


@login_required(login_url='compteuser:login')  
def MissionView(request):
    missions = Mission.objects.all()
    today = datetime.date.today()
    for mission in missions :        
        mission.diff = mission.date_retour.day - mission.date_depart.day
    
    
    context = {
        'missions':missions,
        'today':today
    }
    
    return render(request, 'mission/index.html', context)



@login_required(login_url='compteuser:login')
def Ajout_mission(request):
    projets = Projet.objects.filter(etat = 'EN COURS')
    employes = Employer.objects.filter(etat = 'EN ACTIVITE')
    vehicules = Engins.objects.filter(etat = 'DISPONIBLE')
    
    if request.method == 'POST':
        mission = Mission()
        if request.POST['moyen'] == 'NON' :
            mission.concessionnaire = request.POST['concessionnaire']
            mission.matriculeLouer = request.POST['matriculeLouer']
            mission.moyentransport = "VEHICULE DE LOCATION"
        elif request.POST['moyen'] == 'OUI':
            course = Course()
            course.etat_course = "EN COURS"
            course.motif = request.POST['objet']
            course.depart = request.POST['depart']
            course.destination = request.POST['destination']
            course.date_course = request.POST['date_depart']
            course.vehicule_id = request.POST['vehicule']
            course.employe_id = request.POST['chauffeur']
            course.save()
            
            engin = Engins.objects.get(id = course.vehicule.id)
            engin.etat = 'OCCUPE'
            engin.save()
            
            user = Employer.objects.get(id = course.employe.id)
            user.etat = 'OCCUPE'
            user.save()
            
            mission.course_id = course.id
            mission.moyentransport = "VEHICULE DE SERVICE"
        else:
            return HttpResponseRedirect(reverse('gestions:ajout_mission'))
   
        
        mission.objet = request.POST['objet']
        mission.reference = "/AGRO-MAP/SL/"+str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)
        mission.date_depart = request.POST['date_depart']
        mission.date_retour = request.POST['date_retour']
        mission.localite = request.POST['localite']
        mission.employe_id = request.POST['employe']
        mission.projet_id = request.POST['projet']
        mission.etat_mission = "EN COURS"
        mission.save()
        user = Employer.objects.get(id = mission.employe.id)
        user.etat = 'OCCUPE'
        user.save()
        messages.success(request, "Mission enregistrer avec succèss !")
        return HttpResponseRedirect(reverse('gestions:missions'))
    
        
    context = {
        'projets':projets,
        'employes':employes,
        'vehicules':vehicules,
        
    }
    
    return render(request, 'mission/ajout_mission.html', context)
            


@login_required(login_url='compteuser:login')
def Edit_mission(request, id= None):
    mission = Mission.objects.get(id= id)
    projets = Projet.objects.filter(etat = 'EN COURS')
    employes = Employer.objects.filter(etat = 'EN ACTIVITE')
    vehicules = Engins.objects.filter(etat = 'DISPONIBLE')
    
    context = {
        "mission":mission,
        "projets":projets,
        "employes":employes,
        "vehicules":vehicules
    }
    
    return render(request, 'mission/edit_mission.html',context)
    
 
 
@login_required(login_url='compteuser:login')   
def Finir_mission(request, id = None):
    mission = Mission.objects.get(id = id)
    mission.etat_mission = "TERMINER"
    mission.date_terminer = datetime.date.today()
    mission.save()
    employe = Employer.objects.get(id = mission.employe.id)
    employe.etat = "EN ACTIVITE"
    employe.save()
    
    if not mission.matriculeLouer:
        course = Course.objects.get(id = mission.course.id)
        course.etat_course = 'TERMINER'
        course.date_fin = datetime.datetime.now()
        course.save()
        
        engin = Engins.objects.get(id = course.vehicule.id)
        engin.etat = 'DISPONIBLE'
        engin.save()
        
        user = Employer.objects.get(id = course.employe.id)
        user.etat = 'EN ACTIVITE'
        user.save()


@login_required(login_url='compteuser:login')      
def Delete_mission(request, id = None):
    mission = Mission.objects.get(id = id)
    employe = Employer.objects.get(id = mission.employe.id)
    employe.etat = "EN ACTIVITE"
    employe.save()
    
    if not mission.matriculeLouer:
        course = Course.objects.get(id = mission.course.id)
        engin = Engins.objects.get(id = course.vehicule.id)
        engin.etat = 'DISPONIBLE'
        engin.save()  
        user = Employer.objects.get(id = course.employe.id)
        user.etat = 'EN ACTIVITE'
        user.save()
        
        course.delete()
    
    mission.delete()
    messages.success(request, "Suppression effectué avec succèss !")
    return HttpResponseRedirect(reverse('gestions:missions'))
    


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

# @login_required(login_url='connexion')
def print_mission_pdf(request, id=None):
    mission = get_object_or_404(Mission, id=id)
    template_path = 'mission/mission.html'
    context = {
        'mission': mission,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Mission.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Une Erreure est Survenue, Réessayer SVP...' + html + '</pre>')
    return response





@login_required(login_url='compteuser:login')
def DommageView(request):
    return render(request,'dommage/index.html')