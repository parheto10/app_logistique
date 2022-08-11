from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from equipements.views import AccessoiresView, Ajout_equipement, Attribut_Equipement, Delete_accessoire, DeleteMateriels, Edit_accessoires, Edit_equipement, MaterielView, Restitu_equipement, Store_attribution, Update_accessoire

app_name = "equipements"

urlpatterns = [
    path('index_accessoire/', AccessoiresView, name='accesooires'),
    path('edit_accessoire/<int:id>', Edit_accessoires, name='edit_accessoire'),
    path('delete_accessoire/<int:id>', Delete_accessoire, name='delete_accessoire'),
    path('update_accessoire/', Update_accessoire, name='update_accessoire'),
    
    path('index_materiel/', MaterielView, name='materiels'),
    path('ajout_equipement/', Ajout_equipement, name='ajout_equipement'),
    path('edit_equipement/<int:id>', Edit_equipement, name='edit_equipement'),
    path('supprimer_equipement/<int:id>', DeleteMateriels, name='supprimer_equipement'),
    
    path('attribut_equipement/<int:id>', Attribut_Equipement, name='attribut_equipement'),
    path('restitu_equipement/<int:id>', Restitu_equipement, name='restitu_equipement'),
    path('store_attribution/', Store_attribution, name='store_attribution'),
    
    
]