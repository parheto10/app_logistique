from django.db import models

from parametres.models import Type_vehicule

# Create your models here.
ETAT_ENGINS = (
    ('DISPONIBLE', "DISPONIBLE"),
    ('OCCUPE', "OCCUPE"),
    ('VENDU', "VENDU"),
    ('GARAGE', "GARAGE"),
)


class Engins(models.Model):
    model = models.CharField(max_length=225)
    marque = models.CharField(max_length=225)
    couleur = models.CharField(max_length=225)
    matricule = models.CharField(max_length=225)
    numcharsis = models.CharField(max_length=225,blank=True, null=True)
    date_achat = models.DateField()
    mise_en_circulation = models.DateField()
    prix_achat = models.IntegerField(blank=True, null=True)
    etat = models.CharField(max_length=100, choices=ETAT_ENGINS, default='')
    type_engins = models.ForeignKey(Type_vehicule, on_delete=models.CASCADE)
    engin_image = models.ImageField(blank=True,null=True,upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s - %s" % (self.marque, self.matricule)
    
    def save(self, force_insert=False, force_update=False):
        self.model = self.model.upper()
        self.marque = self.marque.upper()
        self.matricule = self.matricule.upper()
        super(Engins, self).save(force_insert, force_update)
    
    
