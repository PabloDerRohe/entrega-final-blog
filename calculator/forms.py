from django import forms
from django.contrib.auth.models import User



class CalculatorForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    # usuario = forms.ModelChoiceField(queryset=User.objects.all())
    capital_inicial = forms.DecimalField(max_digits=50, decimal_places=2)
    capital_adicional = forms.DecimalField(label='Ahorro mensual', max_digits=50, decimal_places=2)
    interes = forms.DecimalField(label='Interes anual',max_digits=50, decimal_places=2)
    años = forms.IntegerField()


