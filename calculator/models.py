from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CalculadoraInteres(models.Model):
        
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    monto_inicial = models.DecimalField(max_digits=30, decimal_places=2)
    ahorro_mensual = models.DecimalField(max_digits=30, decimal_places=2)
    interes = models.DecimalField(max_digits=30, decimal_places=2)
    acumulado_con_interes = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    acumulado_sin_interes = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    año = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}'