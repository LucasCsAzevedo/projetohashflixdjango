from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario # importando a classe filme dentro do nosso models

# Só fazemos isso porque criamos mais campos para o Usuário
campos = list(UserAdmin.fieldsets) # Por padrão, os campos exibidos são os da classe UserAdmin, fazendo dessa forma criamos uma lista de campos que queremos que seja exibido na página do usuário, no caso campos a mais!
campos.append(
    ('Histórico', {'fields' : ('filmes_vistos',)}) # Estava dando erro quando criei a primeira vez, foi adicionar a vírgula e funcionou
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme) # Adicionando o filmes no painel de admin
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin) # Classe que gerencia nossos usuários