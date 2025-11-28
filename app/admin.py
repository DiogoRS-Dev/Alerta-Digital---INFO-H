from django.contrib import admin # A senha do admin vai ser Pindamonhangaba.Pelotas123
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia
# from .models import Pergunta, Quiz, QuizPergunta


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
    list_display = ("id", "mensagem", "usuario", "data_hora")
    search_fields = ("mensagem", "usuario__nome")


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mensagem', 'usuario', 'data_hora')

    def mensagem(self, obj):
        return obj.descricao[:50] + ('...' if len(obj.descricao) > 50 else '')

    def usuario(self, obj):
        return obj.email or 'Anônimo'

    def data_hora(self, obj):
        return obj.criado_em.strftime('%d/%m/%Y %H:%M')


# @admin.register(Pergunta)
# class PerguntaAdmin(admin.ModelAdmin):
#     list_display = ("id", "pergunta", "nivel")
#     search_fields = ("pergunta",)


# class QuizPerguntaInline(admin.TabularInline):
#     model = QuizPergunta
#     extra = 1


# @admin.register(Quiz)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = ("id", "nota", "usuario", "data_hora")
#     search_fields = ("usuario__nome",)
#     inlines = [QuizPerguntaInline]


# @admin.register(QuizPergunta)
# class QuizPerguntaAdmin(admin.ModelAdmin):
#     list_display = ("id", "quiz", "usuario", "pergunta")
#     search_fields = ("quiz__id", "usuario__nome", "pergunta__pergunta")
