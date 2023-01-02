from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    nombre_de_place = models.PositiveIntegerField()

    def __str__(self):
        return  "Table " + self.id

class Reservation(models.Model):
    nombre_de_place = models.PositiveIntegerField()
    client = models.ForeignKey(User,  on_delete=models.CASCADE)
    date_de_reservation = models.DateField( auto_now_add=True)
    data_d_utilisation = models.DateField()

class Commande(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("Quantité")
    plat = models.ForeignKey("Repas", on_delete=models.CASCADE)
    date_de_commande = models.DateField( auto_now_add=True)
    date_de_livraison = models.DateField()


    def __str__(self):
        return "Reservation de "  + self.client

class Menu(models.Model):
    Nom_du_menu = models.CharField( max_length=50)
    liste_des_plats = models.ManyToManyField("Repas", related_name="repas")
    
    def return_repas(self):
        return  self.liste_des_plats.all()

    def __str__(self):
        return f'{self.Nom_du_menu}'

    def __unicode__(self):
        return f'{self.Nom_du_menu}'

class Name(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


class Repas(models.Model):
    Nom = models.CharField(max_length=50)
    Prix = models.PositiveIntegerField()
    TYPES_RESPAS = [
        ('Entrée','Entrée'),
        ('Résistance','Résistance'),
        ('Boisson','Boisson'),
        ('Sortie','Sortie'),
        ('Désert','Désert'),
    ]
    type_de_plat = models.CharField(choices = TYPES_RESPAS,  max_length=50)
    images = models.ImageField(upload_to='Images_des_respas')
    description = models.TextField()

    def __str__(self):
        return f'{self.Nom} - {self.Prix}'

    def __unicode__(self):
        pass


  
