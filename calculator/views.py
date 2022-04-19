from django.forms import DecimalField
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from .models import Calculadora, CapitalTiempo
from .forms import CalculatorForm
from .utils import get_plot

from django.contrib.auth.decorators import login_required

from django.db.models import Max

# Create your views here.


@login_required
def list_calculator(request):
    
    calc = Calculadora.objects.all()
    
    data = {
        'calc': calc,
    }
    
    return render(request, 'calculator/list_calculator.html', data)

    
@login_required
def create_calculator(request):
    
    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            nuevo_calculo = Calculadora(
                nombre=data['nombre'],
                usuario=request.user,
                capital_inicial=data['capital_inicial'],
                capital_adicional=data['capital_adicional'], 
                interes=data['interes'],
                años=data['años'],
                )
            nuevo_calculo.save()
            
            calculadora = Calculadora.objects.filter(id=nuevo_calculo.id).values()
            datos = calculadora[0]
            monto = float(datos['capital_inicial'])
            adicional = float(datos['capital_adicional'])
            interes = float(datos['interes'])
            años = int(datos['años'])
                
            for año in range(1, años):
                monto = (monto+(adicional*12))*(1 + interes*0.01)
                capital_tiempo = CapitalTiempo(
                        year = año,
                        capital = monto,
                        calc = Calculadora.objects.get(id=nuevo_calculo.id)
                    )
                capital_tiempo.save()
            
            # calculo_sin_interes = data['monto_inicial']+((data['ahorro_mensual']*12)*data['año'])
            return redirect('list_calculator')
    
    form = CalculatorForm()
    
    
    data = {
        'form': form,
    }
    return render(request, 'calculator/create_calculator.html', data)    


@login_required
def graph(request, id):
    
       
    qs = CapitalTiempo.objects.filter(calc=id)
    x = [x.year for x in qs]
    y = [y.capital for y in qs]
    chart = get_plot(x,y)
    
    capital_max = qs.aggregate(Max('capital'))
    capital = capital_max['capital__max']
    
    data = {
        'chart': chart,
        'capital': capital
    }
    return render(request, 'calculator/graph.html', data)  


@login_required
def delete_calculator(request, id):
    
    calc = Calculadora.objects.get(id=id)    
    calc.delete()
    
    return redirect('list_calculator')