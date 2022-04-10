from django import forms
from django.contrib.auth.models import User

from ckeditor.fields import RichTextFormField


class PostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=70)
    contenido = RichTextFormField(required=False)
    autor = forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=False)
    
    
class BuscarPost(forms.Form):
    buscar_post = forms.CharField(label='Buscador', max_length=40)
    