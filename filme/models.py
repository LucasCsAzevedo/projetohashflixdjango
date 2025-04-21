from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Aonde vamos criar as tabelas do banco

LISTA_CATEGORIAS = ( # Minha lista de opções das categorias, a primeira opção de cada tupla é como essa informação vai aparecer dentro do meu banco e a segunda como vai aparecer para o usuário
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)

# Criar os filmes
class Filme(models.Model): # Cada modelo precisa ser uma subclasse dessa classe models.Model
    titulo = models.CharField(max_length=100) # Essa tabela é tipo de caractere com tamanho de 100 caracteres
    thumb = models.ImageField(upload_to='thumb_filmes') # Passo a pasta aonde as imagens de thum estarão para serem carregadas para essa variável
    descricao = models.TextField(max_length=1000) # Essa tabela é tipo de texto com tamanho de 1000 caracteres
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS) # Essa tabela se difere das outras porque possui uma lista de opções que foi definida fora da classe, sendo uma 'lista' de tuplas
    visualizacoes = models.IntegerField(default=0) # Defino um padrão toda vez que criar um filme
    data_criacao = models.DateTimeField(default=timezone.now) # Preenche a data de criação conforme o usuário criar esse filme automaticamente
    
    def __str__(self): # Qual o formato de string de um objeto dessa classe
        return self.titulo # Quando eu adiciono um filme, na listagem de filmes adicionados vai aparecer o título desse filme


# Criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE) # Minha chave estrangeira, sempre colocar ela como primeiro item. Posso usar o ManyToManyField (Muitos para Muitos). FoeringKey (Um para muitos)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


# Criar o usuário
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')