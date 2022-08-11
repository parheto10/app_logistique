from django import forms

from gestions.models import Attribution, Course, Employer, Mission, Projet


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = [
            'nom',
            'prenom',
            'fonction',
            'email',
            'contact',
            'matricule',
            'etat',
        ]
        
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = [
            'sigle',
            'titre',
            'date_debut',
            'date_fin',
            'etat',
            'logo_partenaire',
            'logo_sarl',
        ]
        
class AttributionForm(forms.ModelForm):
    class Meta:
        model = Attribution
        fields = [
            'date_attribution',
        ]
        
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'motif',
            'depart',
            'destination',
            'date_course',
            'etat_course',
            'employe',
            'vehicule',
        ]

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = [
            'objet',
            'reference',
            'localite',
            'matriculeLouer',
            'concessionnaire',
            'date_depart',
            'date_retour',
            'employe',
            'projet',
        ]
        