from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
