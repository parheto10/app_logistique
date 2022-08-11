from datetime import datetime
import datetime
from django.db import models
from engins.models import Engins
from equipements.models import Materiel

from parametres.models import Fonction

# Create your models here.
ETAT = ( 
    ('EN ACTIVITE', "EN ACTIVITE"),
    ('OCCUPE', "OCCUPE"),
    ('DESACTIVE', "DESACTIVE"),
)
ETAT_PROJET = (
    ('EN COURS', "EN COURS"),
    ('TERMINER', "TERMINER"),
)



class Employer(models.Model):
    nom = models.CharField(max_length=255) 
    prenom = models.CharField(max_length=255)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=100, blank=True, null=True)
    matricule = models.CharField(max_length=255, blank=True, null=True)
    materiel = models.ManyToManyField(Materiel, through='Attribution')
    etat = models.CharField(max_length=50, choices=ETAT, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return "%s - %s" % (self.nom, self.prenom)
    
    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenom = self.prenom.upper()
        # self.matricule = self.matricule.upper()
        super(Employer, self).save(force_insert, force_update)
        


class Projet(models.Model):
    sigle = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    etat = models.CharField(max_length=255, choices=ETAT_PROJET,default='')
    logo_partenaire = models.ImageField(blank=True,null=True,upload_to="images/")
    logo_sarl = models.ImageField(blank=True,null=True,upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s - %s" % (self.sigle, self.titre)
    
    def save(self, force_insert=False, force_update=False):
        self.sigle = self.sigle.upper()
        self.titre = self.titre.upper()
        super(Projet, self).save(force_insert, force_update)
        
        
class Attribution(models.Model):
    employe = models.ForeignKey(Employer, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    etat = models.BooleanField(default=False)
    date_attribution = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s - %s" % (self.employe, self.materiel)
    
    
class Course(models.Model):
    etat_course = models.CharField(max_length=255,choices=ETAT_PROJET,default='')
    motif = models.TextField()
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date_course = models.DateField()
    date_fin = models.DateField(blank=True , null=True)
    employe = models.ForeignKey(Employer, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Engins, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s - %s" % (self.depart, self.destination)
    
    def save(self, force_insert=False, force_update=False):
        self.depart = self.depart.upper()
        self.destination = self.destination.upper()
        super(Course, self).save(force_insert, force_update)
        
        
class Mission(models.Model):
    objet = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    localite = models.CharField(max_length=255)
    matriculeLouer = models.CharField(max_length=255, blank=True, null= True) 
    concessionnaire = models.CharField(max_length=255, blank=True, null=True)
    moyentransport = models.CharField(max_length=255, blank=True, null=True)
    date_depart = models.DateField()
    date_retour = models.DateField()
    date_terminer = models.DateField(blank=True , null=True)
    employe = models.ForeignKey(Employer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    etat_mission = models.CharField(max_length=255,choices=ETAT_PROJET,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, force_insert=False, force_update=False):
        self.reference = self.reference.upper()
        super(Mission, self).save(force_insert, force_update)
    
    
    
