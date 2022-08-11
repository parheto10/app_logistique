from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from gestions.views import Ajout_course, Ajout_employe, Ajout_mission, Ajout_projet, CoursesView, Delete_course, Delete_mission, DommageView, Edit_course, Edit_employe, Edit_mission, Edit_projet, EmployeView, Finir_mission, MissionView, ProjetView, Termine_course, print_mission_pdf

app_name = "gestions"

urlpatterns = [
    path('index_employe/', EmployeView, name='employes'),
    path('ajout_employe/', Ajout_employe, name='ajout_employe'),
    path('edit_employe/<int:id>', Edit_employe, name='edit_employe'),
    
    path('index_proj/', ProjetView, name='projets'),
    path('ajout_proj/', Ajout_projet, name='ajout_projet'),
    path('edit_proj/<int:id>', Edit_projet, name='edit_projet'),
    
    path('index_course/', CoursesView, name='courses'),
    path('ajout_course/', Ajout_course, name='ajout_course'),
    path('edit_course/<int:id>', Edit_course, name='edit_course'),
    path('delete_course/<int:id>', Delete_course, name='delete_course'),
    path('termine_course/<int:id>', Termine_course, name='termine_course'),
    
    path('index_mission/', MissionView, name='missions'),
    path('ajout_mission/', Ajout_mission, name='ajout_mission'),
    path('edit_mission/<int:id>', Edit_mission, name='edit_mission'),
    path('finir_mission/<int:id>', Finir_mission, name='finir_mission'), 
    path('print_mission_pdf/<int:id>', print_mission_pdf, name='print_mission_pdf'),
    path('delete_mission/<int:id>', Delete_mission, name='delete_mission'),
    
    path('index_dommage/', DommageView, name='dommages'),
    
]