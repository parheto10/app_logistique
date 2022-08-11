from django.db import models

# Create your models here.

class Fonction(models.Model):
    libelle = models.CharField(max_length=225,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Fonction, self).save(force_insert, force_update)
        
        
class Type_vehicule(models.Model):
    libelle = models.CharField(max_length=225,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Type_vehicule, self).save(force_insert, force_update)
        

class Type_materiel(models.Model):
    libelle = models.CharField(max_length=225,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s' % (self.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Type_materiel, self).save(force_insert, force_update)


