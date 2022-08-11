from django.contrib import admin

from parametres.models import Fonction, Type_materiel, Type_vehicule

# Register your models here.
admin.site.register(Fonction)
admin.site.register(Type_materiel)
admin.site.register(Type_vehicule)
