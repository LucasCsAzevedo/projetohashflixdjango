from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homepage(FormView): # Exibir uma página
    template_name = 'homepage.html'
    form_class = FormHomepage
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes') # Se o usuário estiver logado, redireciono ele para a homefilmes quando ele clicar na logo
        else:
            return super().get(request, *args, **kwargs) # Redireciona para a homepage
        
    
    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView): # Listar objetos, espera receber 2 parâmetros: template e modelo
    template_name = 'homefilmes.html'
    model = Filme
    
    
class Detalhesfilme(LoginRequiredMixin, DetailView): # Exibe uma página com os detalhes de um objeto
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> 1 item do nosso 
    
    
    def get(self, request, *args, **kwargs): # Contabilizando as visualizacoes do filme
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        # Verificar o usuário que está logado
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # Redireciona o usuário para URL final
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    
    
class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme
    
    def get_queryset(self): # Editando o object_list com base na pesquisa do cliente
        termo_pesquisa = self.request.GET.get('query')
        
        if termo_pesquisa:
            object_list = self.model.objects.filter(
                Q(titulo__icontains=termo_pesquisa) |
                Q(descricao__icontains=termo_pesquisa)
                ) # Filtro minha lista de filmes com base no termo de pesquisa do usuário, usando esse padrão __icontains, coloquei essa funcionalidade Q para usar mais de um filtro
            return object_list
        else:
            return None


class Editarperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario # Tabela do banco
    fields = ['first_name', 'last_name', 'email'] # Campos que o usuário vai poder atualizar
    
    
    def get_success_url(self):
        return reverse('filme:homefilmes')
    
    
class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
    
    def get_success_url(self):
        return reverse('filme:login')
 
 
 
   
    
    
    
# Forma que usamos anteriormente
# def homepage(request): # Por padrão precisa receber o request, vai identificar se meu request é do tipo POST ou GET
#     return render(request, 'homepage.html') # Página que queremos apenas exibir um template, chamada de Template View


# def homefilmes(request): # FBV - Functions Base Views
#     context = {}
#     lista_filmes = Filme.objects.all() # Pego todos os objetos do meu Banco de Dados, da Class Filme
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)


# Três passos: URL - View - Template

# FBV - Functions Base Views
'''
    Funções em Python, usado em sites mais simples, você cria todos os processos
'''

# CBV - Class Base Views, mais usado na prática
'''
    Criamos uma classe para nossa página, que precisa herdar uma classe do Django; Já traz muitas coisas prontas, só precisamos saber o que usar
'''

# contex - Contexto da página HTML, dicionário Python que vai passar como parâmetro para página HTMl, que permite que quando chegarmos na nossa página HTML possamos usar tags em Python como tags em bloco {%}