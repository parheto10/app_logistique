from django.db import models

from parametres.models import Type_materiel

# Create your models here.

ETAT_MATERIELS = (
    ('FONCTIONNELLE', "FONCTIONNELLE"),
    ('ENDOMMAGE', "ENDOMMAGE"),
    ('REPARATION', "REPARATION"),
    ('ATTRIBUER', "ATTRIBUER"),
)

class Accessoire(models.Model):
    libelle = models.CharField(max_length=255 ,unique=True)
    date_achat = models.DateField()
    prix_achat = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    destination = models.CharField(max_length=255)
    qty_today = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s" % (self.libelle)
    
    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        self.destination = self.destination.upper()
        super(Accessoire, self).save(force_insert, force_update)
        
        

class Materiel(models.Model):
    code = models.CharField(max_length=255,blank=True, null=True)
    num_serie = models.CharField(max_length=255,blank=True, null=True)
    model = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    etat = models.CharField(max_length=255, choices=ETAT_MATERIELS, default='')
    date_achat = models.DateField()
    quantity = models.IntegerField(default=1)
    prix_achat = models.IntegerField(blank=True, null=True)
    materiel_image = models.ImageField(blank=True,null=True,upload_to="images/")
    type_materiel = models.ForeignKey(Type_materiel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s - %s" % (self.marque,self.num_serie)
    
    def save(self, force_insert=False, force_update=False):
        self.code = self.code.upper()
        self.num_serie = self.num_serie.upper()
        self.model = self.model.upper()
        self.marque = self.marque.upper()
        super(Materiel, self).save(force_insert, force_update)
    
    