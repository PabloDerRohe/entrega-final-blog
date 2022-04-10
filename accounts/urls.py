from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('editar/', views.editar_user, name='editar_user'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
