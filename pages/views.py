from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, BuscarPost

from django.contrib.auth.decorators import login_required

# Create your views here.


def listado_posts(request):
    
    posts = Post.objects.all()
    
    datos = {
        'posts': posts
    }
    
    return render(request, 'pages/listado_posts.html', datos)


def leer_post(request, id):
    
    post = Post.objects.get(id=id)
    
    datos = {
        'post': post
    }
    
    return render(request, 'pages/leer_post.html', datos)


def buscar_post(request):
    
    post_buscados = []
    dato = request.GET.get('buscar_post', None)
            
    if dato is not None:
        post_buscados = Post.objects.filter(titulo=dato)
    
    buscador = BuscarPost()
        
    return render(
        request, "pages/buscar_post.html",
        {'buscador': buscador, 'post_buscados': post_buscados, 'dato': dato})


@login_required
def crear_post(request):
    
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nuevo_post = Post(
                titulo=data['titulo'],
                subtitulo=data['subtitulo'],
                contenido=data['contenido'],
                autor=data['autor'], 
                imagen=data['imagen'],
                )
            
            nuevo_post.save()
            return redirect('listado_posts')
            
    formulario = PostForm()
    return render(request, 'pages/crear_post.html', {'formulario': formulario})



@login_required
def editar_post(request, id):
    
    post = Post.objects.get(id=id)    
    
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            
            data = formulario.cleaned_data #Limpia informacion
            
            post.titulo = data['titulo']
            post.subtitulo = data['subtitulo']
            post.contenido = data['contenido']
            post.autor = data['autor']
            post.imagen = data['imagen']
            post.save()
            
            return redirect('listado_posts')
            
    formulario = PostForm(
        initial={
            'titulo': post.titulo,
            'subtitulo': post.subtitulo,
            'contenido': post.contenido,
            'autor': post.autor,
            'imagen': post.imagen,
        }
    )
    return render(
        request, 'pages/editar_post.html',
        {'formulario': formulario, 'post': post})


@login_required
def borrar_post(request, id):
    
    post = Post.objects.get(id=id)    
    post.delete()
    
    return redirect('listado_posts')
    