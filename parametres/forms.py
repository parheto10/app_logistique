from django import forms
from parametres.models import Fonction,Type_materiel, Type_vehicule

class FonctionForm(forms.ModelForm):
    class Meta:
        model = Fonction
        fields = [
            'libelle',
        ]
        
class Type_materialForm(forms.ModelForm):
    class Meta:
        model = Type_materiel
        fields = [
            'libelle',
        ]
        
class Type_vehiculeForm(forms.ModelForm):
    class Meta:
        model = Type_vehicule
        fields = [
            'libelle',
        ]