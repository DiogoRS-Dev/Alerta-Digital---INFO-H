from django.contrib import admin # A senha do admin vai ser Pindamonhangaba.Pelotas123
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia
from .models import Pergunta, Quiz, QuizPergunta, Alternativa


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf", "email", "data_nasc")
    search_fields = ("nome", "cpf", "email")


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ("id", "setor", "usuario")
    search_fields = ("setor", "usuario__nome")


@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "data_hora")
    search_fields = ("usuario__nome",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'apelido', 'usuario', 'criado_em')
    search_fields = ("texto", "usuario__nome")


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao_curta', 'email_usuario', 'data_hora')  # <-- CORRIGIDO

    # Renomeei métodos para evitar conflito com nomes reais
    def descricao_curta(self, obj):
        return obj.descricao[:50] + ('...' if len(obj.descricao) > 50 else '')

    def email_usuario(self, obj):
        return obj.email or 'Anônimo'

    def data_hora(self, obj):
        return obj.criado_em.strftime('%d/%m/%Y %H:%M')

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 3

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pergunta', 'nivel')
    search_fields = ("pergunta",)
    inlines = [AlternativaInline]

@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pergunta', 'texto', 'correta')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nota', 'data_hora')
    search_fields = ("usuario__nome",)

@admin.register(QuizPergunta)
class QuizPerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'usuario', 'pergunta')
    search_fields = ("quiz__id", "usuario__nome", "pergunta__pergunta")
