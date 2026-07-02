from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormCadastro(UserCreationForm):
    class Meta:
        model =  Usuario
        fields = ['first_name','last_name','email','username']