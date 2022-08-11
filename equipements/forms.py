from django import forms
from equipements.models import Accessoire,Materiel



class AccessoireForm(forms.ModelForm):
    class Meta:
        model = Accessoire
        fields = [
            'libelle',
            'date_achat',
            'prix_achat',
            'quantity',
            'destination',
            'qty_today',
        ]
        

class MaterielsForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = [
            'code',
            'num_serie',
            'marque',
            'model',
            'etat',
            'date_achat',
            'quantity',
            'prix_achat',
            'type_materiel',
            'materiel_image',
        ]