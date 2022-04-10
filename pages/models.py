from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=70)
    contenido = RichTextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.titulo} {str(self.autor)}'

