from django.shortcuts import render, redirect

from .models import CalculadoraInteres
from calculator.forms import CalculatorForm

# Create your views here.


def calculator(request):
    
    if request.method == 'POST':
        form = CalculatorForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            
            i=0
            monto = data['monto_inicial']
            
            while i < data['año']:
                monto = (monto+(data['ahorro_mensual']*12))*(1+data['interes']*0.01)
                i = i + 1
                calculo_con_interes = {i: monto}
                
            
            calculo_sin_interes = data['monto_inicial']+((data['ahorro_mensual']*12)*data['año'])
            
            nuevo_post = CalculadoraInteres(
                nombre=data['nombre'],
                usuario=data['usuario'],
                monto_inicial=data['monto_inicial'],
                ahorro_mensual=data['ahorro_mensual'], 
                interes=data['interes'],
                acumulado_con_interes=calculo_con_interes,
                acumulado_sin_interes=calculo_sin_interes,
                año=data['año'],
                )
            
            nuevo_post.save()
            return redirect('listado_posts')
            
    form = CalculatorForm()
    return render(request, 'calculator/calculator.html', {'form': form})
