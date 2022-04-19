from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_calculator, name='list_calculator'),
    path('crear_calculadora/', views.create_calculator, name='create_calculator'),
    path('grafico/<int:id>', views.graph, name='graph'),
    path('borrar_calculadora/<int:id>', views.delete_calculator, name='delete_calculator'),

]
