from ast import Pass
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Calculadora(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    capital_inicial = models.DecimalField(max_digits=50, decimal_places=2)
    capital_adicional = models.DecimalField(max_digits=50, decimal_places=2)
    interes = models.DecimalField(max_digits=50, decimal_places=2)
    años = models.IntegerField()

    def __str__(self):
        return f'{self.id} | {self.nombre}'

class CapitalTiempo(models.Model):
    year = models.IntegerField()
    capital = models.DecimalField(max_digits=50, decimal_places=2)
    calc = models.ForeignKey(Calculadora, on_delete=models.CASCADE, related_name='capitaltiempo')
    
    def __str__(self):
        return f'{self.calc} | {self.year} = {self.capital}'

