from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.listado_posts.as_view(), name='listado_posts'),
    path('leer-post/<int:pk>', views.leer_post.as_view(), name='leer_post'),
    path('crear-post/', views.crear_post.as_view(), name='crear_post'),
    path('editar-post/<int:pk>', views.editar_post.as_view(), name='editar_post'),
    path('borrar-post/<int:pk>', views.borrar_post.as_view(), name='borrar_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
]
