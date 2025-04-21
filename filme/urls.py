from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Editarperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'filme' # Uso esse name como parâmetro na minha URL no arquivo url do meu app, AULA 23 criando links personalizados

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'), # Como para cada detalhe de filme temos um nome, é necessário criar dessa forma, pk é o primary key
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Editarperfil.as_view(), name='editarperfil'), # Preciso passar o pk do usuário para que o django saiba qual usuário vai ser alterado, caso preciso
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]
