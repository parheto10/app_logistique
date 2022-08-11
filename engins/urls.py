from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from engins.views import AjoutCarView, DeleteCars, EditCarView, home

app_name = "engins"

urlpatterns = [
    path('', home, name='home'),
    path('ajout_car/', AjoutCarView, name='ajout_car'),
    path('edit_car/<int:id>', EditCarView, name='edit_car'),
    path('delete_car/<int:id>', DeleteCars, name='deletecar'),
]