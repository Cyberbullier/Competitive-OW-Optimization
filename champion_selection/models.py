from django.db import models
from team import Team
from collections import Counter

# Create your models here.

class ChampionComposition(models.Model):
    """
    use this class to represent database model of clients team composition
    and his/her opponents

    """
    token = models.CharField(max_length=250, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    # all hero models
    ana = models.IntegerField(default=0)
    ashe = models.IntegerField(default=0)
    bastion = models.IntegerField(default=0)
    baptiste = models.IntegerField(default=0)
    brigitte = models.IntegerField(default=0)
    doomfist = models.IntegerField(default=0)
    dva = models.IntegerField(default=0)
    genji = models.IntegerField(default=0)
    hammond = models.IntegerField(default=0)
    hanzo = models.IntegerField(default=0)
    junkrat = models.IntegerField(default=0)
    lucio = models.IntegerField(default=0)
    mcree = models.IntegerField(default=0)
    mei = models.IntegerField(default=0)
    mercy = models.IntegerField(default=0)
    moira = models.IntegerField(default=0)
    orisa = models.IntegerField(default=0)
    pharah = models.IntegerField(default=0)
    reaper = models.IntegerField(default=0)
    reinhardt = models.IntegerField(default=0)
    roadhog = models.IntegerField(default=0)
    sigma = models.IntegerField(default=0)
    soldier76 = models.IntegerField(default=0)
    sombra = models.IntegerField(default=0)
    symmetra = models.IntegerField(default=0)
    torbjorn = models.IntegerField(default=0)
    tracer = models.IntegerField(default=0)
    widowmaker = models.IntegerField(default=0)
    winston = models.IntegerField(default=0)
    zarya = models.IntegerField(default=0)
    zenyatta = models.IntegerField(default=0)





    class Meta:
        # name of db table for this Model
        db_table = 'ChampionComposition'
    
    
    
    
    
    
    
    
    def __str___(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CAD price")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return (self.quantity * self.price)

    def __str__(self):
        return str(self.id)




