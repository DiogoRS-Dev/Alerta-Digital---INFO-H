from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.utils import timezone
from .models import Usuario, Administrador, Acesso, Denuncia, ChatMensagem, Pergunta, Quiz, QuizPergunta, Alternativa
from .forms import (
    UsuarioForm, AdministradorForm, AcessoForm, MensagemForm,
    DenunciaForm, PerguntaForm, QuizForm, QuizPerguntaForm, LoginForm
)
from django.contrib.auth.decorators import login_required
import random


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class PrincipalView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Principal.html')

    
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
class ChatMensagemListView(ListView):
    model = ChatMensagem
    template_name = "mensagens/list.html"   # mantive o caminho antigo para não quebrar links; ajuste se necessário
    context_object_name = "mensagens"


class ChatMensagemCreateView(CreateView):
    model = ChatMensagem
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

def quiz_inicio(request):
    # buscar todas as perguntas ativas
    perguntas_qs = list(Pergunta.objects.all().values_list('id', flat=True))
    if not perguntas_qs:
        # sem perguntas
        return render(request, 'quiz/sem_perguntas.html')

    # embaralhar (opcional)
    random.shuffle(perguntas_qs)

    # guardar na sessão
    request.session['quiz_perguntas'] = perguntas_qs
    request.session['quiz_index'] = 0
    request.session['quiz_score'] = 0
    request.session.modified = True

    # redireciona para a primeira pergunta
    return redirect('quiz_pergunta', pergunta_id=perguntas_qs[0])


# Mostrar/Processar uma pergunta
def quiz_pergunta(request, pergunta_id):
    # carregar sessão
    perguntas = request.session.get('quiz_perguntas')
    index = request.session.get('quiz_index', 0)
    score = request.session.get('quiz_score', 0)

    if not perguntas:
        return redirect('quiz_inicio')  # sessão inválida

    # garantir que a pergunta atual bate com o índice (evita acesso direto fora de ordem)
    try:
        pergunta_atual_id = perguntas[index]
    except IndexError:
        return redirect('quiz_fim')

    if int(pergunta_id) != int(pergunta_atual_id):
        # redireciona para a pergunta correta
        return redirect('quiz_pergunta', pergunta_id=pergunta_atual_id)

    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    alternativas = list(pergunta.alternativas.all())

    # embaralhar alternativas para que ordem mude
    random.shuffle(alternativas)

    if request.method == 'POST':
        escolha_id = request.POST.get('alternativa')
        if not escolha_id:
            # nenhum valor escolhido — volte mostrando erro simples
            return render(request, 'quiz/quiz_pergunta.html', {
                'pergunta': pergunta,
                'alternativas': alternativas,
                'erro': 'Selecione uma alternativa antes de enviar.'
            })

        # validar a alternativa
        try:
            escolha = Alternativa.objects.get(id=escolha_id, pergunta=pergunta)
        except Alternativa.DoesNotExist:
            return render(request, 'quiz/quiz_pergunta.html', {
                'pergunta': pergunta,
                'alternativas': alternativas,
                'erro': 'Alternativa inválida.'
            })

        # atualizar pontuação
        if escolha.correta:
            score += 1
            request.session['quiz_score'] = score

        # avançar índice
        request.session['quiz_index'] = index + 1
        request.session.modified = True

        # se acabou
        if request.session['quiz_index'] >= len(perguntas):
            return redirect('quiz_fim')

        # senão, ir para próxima pergunta
        proxima_id = perguntas[request.session['quiz_index']]
        return redirect('quiz_pergunta', pergunta_id=proxima_id)

    # GET — renderiza pergunta
    return render(request, 'quiz/quiz_pergunta.html', {
        'pergunta': pergunta,
        'alternativas': alternativas,
        'index': index,
        'total': len(perguntas)
    })


# Tela final — exibe resultado e salva no banco se possível
def quiz_fim(request):
    score = request.session.get('quiz_score', 0)
    perguntas = request.session.get('quiz_perguntas', [])
    total = len(perguntas)

    # salvar resultado se usuário estiver logado via sessão manual
    usuario_obj = None
    if 'usuario_id' in request.session:
        try:
            usuario_obj = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            usuario_obj = None

    if usuario_obj:
        # criar Quiz
        quiz = Quiz.objects.create(nota=score, usuario=usuario_obj, data_hora=timezone.now())

        # criar entradas QuizPergunta (registro do quiz)
        for pid in perguntas:
            QuizPergunta.objects.create(quiz=quiz, usuario=usuario_obj, pergunta_id=pid)

    # limpar sessão relacionada ao quiz (opcional)
    request.session.pop('quiz_perguntas', None)
    request.session.pop('quiz_index', None)
    request.session.pop('quiz_score', None)

    return render(request, 'quiz/quiz_fim.html', {
        'score': score,
        'total': total,
        'salvo': bool(usuario_obj)
    })


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


# Funções de chat usadas pelo front (mantive as suas)
def get_usuario_logado(request):
    """Retorna o objeto Usuario baseado na sessão manual."""
    if 'usuario_id' in request.session:
        return Usuario.objects.get(id=request.session['usuario_id'])
    return None


def chat_view(request):
    usuario = get_usuario_logado(request)
    # buscar mensagens raíz (pai is null) ordenadas (o modelo já tem ordering)
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

    pai = get_object_or_404(ChatMensagem, id=mensagem_id)

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