from django import forms
from engins.models import Engins


class EnginsForm(forms.ModelForm):
    class Meta:
        model = Engins
        fields = [
            'model',
            'marque',
            'couleur',
            'matricule',
            'numcharsis',
            'date_achat',
            'mise_en_circulation',
            'prix_achat',
            'etat',
            'type_engins',
            'engin_image',
        ]
        