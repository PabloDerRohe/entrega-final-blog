from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, BuscarPost

from django.contrib.auth.mixins import LoginRequiredMixin




class listado_posts(ListView):
    model = Post
    template_name = 'pages/listado_posts.html'


class leer_post(DetailView):
    
    model = Post
    template_name = 'pages/leer_post.html'


   
class crear_post(LoginRequiredMixin, CreateView):
    
    model = Post     
    template_name= 'pages/crear_post.html'
    # form = PostForm()
    fields = [
        'titulo',
        'subtitulo',
        'contenido',
        'autor',
        'imagen',
        ]
    

class editar_post(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'pages/editar_post.html'
    fields = [
        'titulo',
        'subtitulo',
        'contenido',
        'imagen',
    ] 


class borrar_post(LoginRequiredMixin, DeleteView):
    model = Post     
    template_name= 'pages/borrar_post.html'
    success_url = reverse_lazy('listado_posts')


class buscar_post(ListView):
    model = Post
    template_name = "pages/buscar_post.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(titulo__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
   