from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia, Pergunta, Quiz, QuizPergunta
from .forms import (
    UsuarioForm, AdministradorForm, AcessoForm, MensagemForm,
    DenunciaForm, PerguntaForm, QuizForm, QuizPerguntaForm
)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
    
# ---------------------------
# USUÁRIO
# ---------------------------
class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuarios/list.html"
    context_object_name = "usuarios"


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuarios/detail.html"
    context_object_name = "usuario"


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuarios/form.html"
    success_url = reverse_lazy("usuario_list")


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuarios/form.html"
    success_url = reverse_lazy("usuario_list")


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuarios/confirm_delete.html"
    success_url = reverse_lazy("usuario_list")


# ---------------------------
# ADMINISTRADOR
# ---------------------------
class AdministradorListView(ListView):
    model = Administrador
    template_name = "administradores/list.html"
    context_object_name = "administradores"


class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "administradores/form.html"
    success_url = reverse_lazy("administrador_list")


class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "administradores/form.html"
    success_url = reverse_lazy("administrador_list")


class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = "administradores/confirm_delete.html"
    success_url = reverse_lazy("administrador_list")


# ---------------------------
# ACESSO
# ---------------------------
class AcessoListView(ListView):
    model = Acesso
    template_name = "acessos/list.html"
    context_object_name = "acessos"


class AcessoCreateView(CreateView):
    model = Acesso
    form_class = AcessoForm
    template_name = "acessos/form.html"
    success_url = reverse_lazy("acesso_list")


# ---------------------------
# MENSAGEM
# ---------------------------
class MensagemListView(ListView):
    model = Mensagem
    template_name = "mensagens/list.html"
    context_object_name = "mensagens"


class MensagemCreateView(CreateView):
    model = Mensagem
    form_class = MensagemForm
    template_name = "mensagens/form.html"
    success_url = reverse_lazy("mensagem_list")


# ---------------------------
# DENÚNCIA
# ---------------------------
class DenunciaListView(ListView):
    model = Denuncia
    template_name = "denuncias/list.html"
    context_object_name = "denuncias"


class DenunciaCreateView(CreateView):
    model = Denuncia
    form_class = DenunciaForm
    template_name = "denuncias/form.html"
    success_url = reverse_lazy("denuncia_list")


# ---------------------------
# PERGUNTA
# ---------------------------
class PerguntaListView(ListView):
    model = Pergunta
    template_name = "perguntas/list.html"
    context_object_name = "perguntas"


class PerguntaCreateView(CreateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = "perguntas/form.html"
    success_url = reverse_lazy("pergunta_list")


# ---------------------------
# QUIZ
# ---------------------------
class QuizListView(ListView):
    model = Quiz
    template_name = "quizzes/list.html"
    context_object_name = "quizzes"


class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = "quizzes/form.html"
    success_url = reverse_lazy("quiz_list")


# ---------------------------
# QUIZ-PERGUNTA
# ---------------------------
class QuizPerguntaListView(ListView):
    model = QuizPergunta
    template_name = "quiz_perguntas/list.html"
    context_object_name = "quiz_perguntas"


class QuizPerguntaCreateView(CreateView):
    model = QuizPergunta
    form_class = QuizPerguntaForm
    template_name = "quiz_perguntas/form.html"
    success_url = reverse_lazy("quiz_pergunta_list")
