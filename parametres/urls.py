from django.urls import path, include

from parametres.views import delFonction, delTymateriel, delVehicule, fonctionhomne, typeMaterialhomne, typeVehiculehomne, upFonction, upTymateriel, upVehicule, updateFonction, updateTymateriel, updateVehicule

app_name = "parametres"

urlpatterns = [
    path('fonction/', fonctionhomne, name='fonction'),
    path('type-material/', typeMaterialhomne, name='typem'),
    path('type-vehicule/', typeVehiculehomne, name='tyvehicule'),
    
    path('del-fonction/<int:id>', delFonction, name='delfonction'),
    path('up-fonction/<int:id>', upFonction, name='upfonction'),
    path('update-fonction/', updateFonction, name='update_fonction'),
    
    path('del-tymateriel/<int:id>', delTymateriel, name='deltymateriel'),
    path('up-tymateriel/<int:id>', upTymateriel, name='uptymateriel'),
    path('update-tymateriel/', updateTymateriel, name='update_tymateriel'),    
    
    path('del-delvehicule/<int:id>', delVehicule, name='delvehicule'),
    path('up-vehicule/<int:id>', upVehicule, name='upvehicule'),
    path('update-vehicule/', updateVehicule, name='update_vehicule'),

    
    
    # path('', connexion, name='connexion'),
    # path('inscription/', inscription, name='inscription'),
    # path('deconnexion/', deconnexion, name='deconnexion'),
    # path('responsables/', responsable, name='responsables'),
    # path('projets/', projet, name='projets'),
    # path('add_projet/', add_projet, name='add_projet'),
    # path('techniciens/', technicien, name='techniciens'),
    # path('add_technicien/', add_technicien, name='add_technicien'),
    # path('projet/<int:id>', detail_projet, name='detail_projet'),
    # path('accueil/', index, name='index'),
]