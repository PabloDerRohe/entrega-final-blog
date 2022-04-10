from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_posts, name='listado_posts'),
    path('leer-post/<int:id>', views.leer_post, name='leer_post'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
    path('editar-post/<int:id>', views.editar_post, name='editar_post'),
    path('borrar-post/<int:id>', views.borrar_post, name='borrar_post'),
]
