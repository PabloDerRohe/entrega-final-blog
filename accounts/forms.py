from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NuestraCreacionUser(UserCreationForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", max_length=20, required=False)
    last_name = forms.CharField(label="Apellido", max_length=20, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = { k: '' for k in fields }
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NuestraEdicionUser(forms.Form):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(), required=False)
    first_name = forms.CharField(label="Nombre", max_length=20, required=False)
    last_name = forms.CharField(label="Apellido", max_length=20, required=False)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(label="Link", required=False)
    more_description = forms.CharField(label="Descripcion", max_length=100, required=False)
    