from django.shortcuts import render
from pages.models import Post

# Create your views here.

def index(request):
    
    posts = Post.objects.all()
    
    return render(request, 'index/index.html', {'posts': posts})

def about(request):
    return render(request, 'index/about.html', {})
