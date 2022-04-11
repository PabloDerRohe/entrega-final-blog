from django import forms
from django.contrib.auth.models import User


class CalculatorForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    monto_inicial = forms.DecimalField(max_digits=30, decimal_places=2)
    ahorro_mensual = forms.DecimalField(max_digits=30, decimal_places=2)
    interes = forms.DecimalField(max_digits=30, decimal_places=2)
    # acumulado_con_interes = forms.DecimalField(max_digits=30, decimal_places=2)
    # acumulado_sin_interes = forms.DecimalField(max_digits=30, decimal_places=2)
    año = forms.IntegerField()