from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    nombre_de_place = models.PositiveIntegerField()

    def __str__(self): 
        return  "Table " + str(self.id)

class Reservation(models.Model):
    nombre_de_place = models.PositiveIntegerField()
    client = models.ForeignKey(User,  on_delete=models.CASCADE)
    date_de_reservation = models.DateField( auto_now_add=True)
    data_d_utilisation = models.DateField()

    def __str__(self):
        return "Reservation de "  + self.client

class Commande(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("Quantité")
    plat = models.ForeignKey("Repas", on_delete=models.CASCADE)
    date_de_commande = models.DateField( auto_now_add=True)
    TYPE_COMMANDE =  [('En cours','En cours'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')]
    etat = models.CharField(choices = TYPE_COMMANDE, default = 'En cours' , max_length=50)
    date_de_livraison = models.DateField()

    

class Commande_menu(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("Quantité")
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    date_de_commande = models.DateField( auto_now_add=True)
    date_de_livraison = models.DateField()
    TYPE_COMMANDE =  [('En cours','En cours'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')]
    etat = models.CharField(choices = TYPE_COMMANDE, default = 'En cours' , max_length=50)

class Menu(models.Model):
    Nom_du_menu = models.CharField( max_length=50)
    liste_des_plats = models.ManyToManyField("Repas", related_name="repas")
    
    def return_repas(self):
        return  self.liste_des_plats.all()
    def return_first(self):
        plats = self.liste_des_plats.all()
        return plats[0]
    def get_total_price(self):
        plats = self.liste_des_plats.all()
        somme = 0
        for item in plats:
            somme = somme + item.Prix
        return somme

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


  
