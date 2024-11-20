# forms.py
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm

class newContraseñaForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña Actual')
    new_password = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña')
    new_password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Nueva Contraseña')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise forms.ValidationError("Las nuevas contraseñas no coinciden.")

