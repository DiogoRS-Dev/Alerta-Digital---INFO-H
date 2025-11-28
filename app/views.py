from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia, ChatMensagem
from .forms import (
    UsuarioForm, AdministradorForm, AcessoForm, MensagemForm,
    DenunciaForm, PerguntaForm, QuizForm, QuizPerguntaForm, LoginForm
)
from django.contrib.auth.decorators import login_required
# from .models import Pergunta, Quiz, QuizPergunta


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
    
# ---------------------------
# USUÁRIO
# ---------------------------
def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = form.cleaned_data['senha']  # pode criptografar depois
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                usuario = Usuario.objects.get(email=email, senha=senha)
                request.session['usuario_id'] = usuario.id   # login manual
                messages.success(request, "Login realizado!")
                return redirect('dashboard')
            except Usuario.DoesNotExist:
                messages.error(request, "Email ou senha incorretos.")

    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })


def dashboard(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    return render(request, 'dashboard.html', { 'usuario': usuario })


def logout_view(request):
    request.session.flush()
    return redirect('login')

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

def fazer_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)

        if form.is_valid():
            denuncia = form.save()
            return redirect('denuncia_sucesso')
        else:
            print(form.errors)  # DEBUG
    else:
        form = DenunciaForm()

    return render(request, 'denuncias/form.html', {'form': form})

def denuncia_sucesso(request):
    return render(request, 'denuncias/sucesso.html')

# ---------------------------
# PERGUNTA
# ---------------------------
# class PerguntaListView(ListView):
#     model = Pergunta
#     template_name = "perguntas/list.html"
#     context_object_name = "perguntas"


# class PerguntaCreateView(CreateView):
#     model = Pergunta
#     form_class = PerguntaForm
#     template_name = "perguntas/form.html"
#     success_url = reverse_lazy("pergunta_list")


# # ---------------------------
# # QUIZ
# # ---------------------------
# class QuizListView(ListView):
#     model = Quiz
#     template_name = "quizzes/list.html"
#     context_object_name = "quizzes"


# class QuizCreateView(CreateView):
#     model = Quiz
#     form_class = QuizForm
#     template_name = "quizzes/form.html"
#     success_url = reverse_lazy("quiz_list")


# # ---------------------------
# # QUIZ-PERGUNTA
# # ---------------------------
# class QuizPerguntaListView(ListView):
#     model = QuizPergunta
#     template_name = "quiz_perguntas/list.html"
#     context_object_name = "quiz_perguntas"


# class QuizPerguntaCreateView(CreateView):
#     model = QuizPergunta
#     form_class = QuizPerguntaForm
#     template_name = "quiz_perguntas/form.html"
#     success_url = reverse_lazy("quiz_pergunta_list")


# ---------------------------
# PÁGINAS DE GOLPES
# ---------------------------
class GolpeView(View):
    def get(self, request, golpe_nome):
        template_name = f"tipos_golpes/{golpe_nome}.html"
        return render(request, template_name)



def get_usuario_logado(request):
    """Retorna o objeto Usuario baseado na sessão manual."""
    if 'usuario_id' in request.session:
        return Usuario.objects.get(id=request.session['usuario_id'])
    return None


def chat_view(request):
    usuario = get_usuario_logado(request)

    mensagens = ChatMensagem.objects.filter(pai__isnull=True)

    if request.method == "POST":
        if not usuario:
            messages.error(request, "Você precisa estar logado para comentar.")
            return redirect("login")

        texto = request.POST.get("texto")
        apelido = request.POST.get("apelido")

        ChatMensagem.objects.create(
            usuario=usuario,
            apelido=apelido,
            texto=texto
        )

        return redirect("chat")

    return render(request, "chat/chat.html", {
        "mensagens": mensagens,
        "usuario": usuario
    })


def chat_responder(request, mensagem_id):
    usuario = get_usuario_logado(request)

    pai = ChatMensagem.objects.get(id=mensagem_id)

    if request.method == "POST":
        texto = request.POST.get("texto")
        apelido = request.POST.get("apelido")

        ChatMensagem.objects.create(
            usuario=usuario,
            apelido=apelido,
            texto=texto,
            pai=pai
        )

    return redirect("chat")