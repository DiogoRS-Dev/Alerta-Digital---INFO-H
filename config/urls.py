from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from app import views
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
    DenunciaListView, DenunciaCreateView, fazer_denuncia, denuncia_sucesso,
    # Pergunta
    PerguntaListView, PerguntaCreateView,
    # Quiz
    QuizListView, QuizCreateView,
    # QuizPergunta
    QuizPerguntaListView, QuizPerguntaCreateView,
    # Golpes
    GolpeView
)

app_name = "Alerta_Digital"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # Usuários
    path("usuarios/", UsuarioListView.as_view(), name="usuario_list"),
    path("usuarios/<int:pk>/", UsuarioDetailView.as_view(), name="usuario_detail"),
    path("usuarios/novo/", UsuarioCreateView.as_view(), name="usuario_create"),
    path("usuarios/<int:pk>/editar/", UsuarioUpdateView.as_view(), name="usuario_update"),
    path("usuarios/<int:pk>/deletar/", UsuarioDeleteView.as_view(), name="usuario_delete"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

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
    path('denunciar/', fazer_denuncia, name='fazer_denuncia'),
    path('denuncia/sucesso/', denuncia_sucesso, name='denuncia_sucesso'),

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
    path("tipos_golpes/<str:golpe_nome>/", GolpeView.as_view(), name="golpe_detail"),

    path("chat/", views.chat_view, name="chat"),
    path("chat/responder/<int:mensagem_id>/", views.chat_responder, name="chat_responder"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

