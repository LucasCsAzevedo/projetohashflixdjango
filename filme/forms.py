from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField() # Se passar o EmailField sem nenhum parâmetro dentro dos parênteses se torna um campo obrigatório, se quiser que seja opcional uso o required=False
    
    
    class Meta: # Modelo para criar um usuário, como já temos um padrão de formulário de Usuário, importamos ele
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2') # Nome, E-mail, Crie sua senha, Confirme sua senha