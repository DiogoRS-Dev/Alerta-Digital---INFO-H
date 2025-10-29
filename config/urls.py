from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from app.views import (
    IndexView,
    # Usuário
    UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    # Administrador
    AdministradorListView, AdministradorCreateView, AdministradorUpdateView, AdministradorDeleteView,
    # Acesso
    AcessoListView, AcessoCreateView,
    # Mensagem
    MensagemListView, MensagemCreateView,
    # Denúncia
    DenunciaListView, DenunciaCreateView,
    # Pergunta
    PerguntaListView, PerguntaCreateView,
    # Quiz
    QuizListView, QuizCreateView,
    # QuizPergunta
    QuizPerguntaListView, QuizPerguntaCreateView
)

app_name = "Alerta_Digital"  # substitua "app" pelo nome do seu ap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # Usuários
    path("usuarios/", UsuarioListView.as_view(), name="usuario_list"),
    path("usuarios/<int:pk>/", UsuarioDetailView.as_view(), name="usuario_detail"),
    path("usuarios/novo/", UsuarioCreateView.as_view(), name="usuario_create"),
    path("usuarios/<int:pk>/editar/", UsuarioUpdateView.as_view(), name="usuario_update"),
    path("usuarios/<int:pk>/deletar/", UsuarioDeleteView.as_view(), name="usuario_delete"),

    # Administradores
    path("administradores/", AdministradorListView.as_view(), name="administrador_list"),
    path("administradores/novo/", AdministradorCreateView.as_view(), name="administrador_create"),
    path("administradores/<int:pk>/editar/", AdministradorUpdateView.as_view(), name="administrador_update"),
    path("administradores/<int:pk>/deletar/", AdministradorDeleteView.as_view(), name="administrador_delete"),

    # Acessos
    path("acessos/", AcessoListView.as_view(), name="acesso_list"),
    path("acessos/novo/", AcessoCreateView.as_view(), name="acesso_create"),

    # Mensagens
    path("mensagens/", MensagemListView.as_view(), name="mensagem_list"),
    path("mensagens/nova/", MensagemCreateView.as_view(), name="mensagem_create"),

    # Denúncias
    path("denuncias/", DenunciaListView.as_view(), name="denuncia_list"),
    path("denuncias/nova/", DenunciaCreateView.as_view(), name="denuncia_create"),
    path('denunciar/', views.fazer_denuncia, name='fazer_denuncia'),
    path('denuncia/sucesso/', views.denuncia_sucesso, name='denuncia_sucesso'),

    # Perguntas
    path("perguntas/", PerguntaListView.as_view(), name="pergunta_list"),
    path("perguntas/nova/", PerguntaCreateView.as_view(), name="pergunta_create"),

    # Quizzes
    path("quizzes/", QuizListView.as_view(), name="quiz_list"),
    path("quizzes/novo/", QuizCreateView.as_view(), name="quiz_create"),

    # QuizPergunta
    path("quiz-perguntas/", QuizPerguntaListView.as_view(), name="quiz_pergunta_list"),
    path("quiz-perguntas/nova/", QuizPerguntaCreateView.as_view(), name="quiz_pergunta_create"),

        # Páginas de golpes
    path("tipos_golpes/<str:golpe_nome>/", 
         IndexView.as_view() if False else 
         __import__('app.views', fromlist=['GolpeView']).GolpeView.as_view(),
         name="golpe_detail"),


#--------------------------------------------------------------------------------------------------------------------------------

]
