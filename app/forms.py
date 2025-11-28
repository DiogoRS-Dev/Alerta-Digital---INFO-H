from django import forms
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia
# from .models import Pergunta, Quiz, QuizPergunta

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'data_nasc', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ["setor", "usuario"]


class AcessoForm(forms.ModelForm):
    class Meta:
        model = Acesso
        fields = ["usuario", "data_hora"]


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["mensagem", "data_hora", "usuario"]


class DenunciaForm(forms.ModelForm):
    consentimento = forms.BooleanField(
        required=True,
        label="Concordo que as informações serão usadas para investigação"
    )

    class Meta:
        model = Denuncia
        fields = ['categoria', 'descricao', 'email', 'anexo']  # REMOVER consentimento


# class PerguntaForm(forms.ModelForm):
#     class Meta:
#         model = Pergunta
#         fields = ["pergunta", "nivel"]

#     def clean_nivel(self):
#         nivel = self.cleaned_data["nivel"]
#         if nivel < 1:
#             raise forms.ValidationError("O nível deve ser maior que 0.")
#         return nivel


# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = ["nota", "data_hora", "usuario", "perguntas"]

#     def clean_nota(self):
#         nota = self.cleaned_data["nota"]
#         if nota < 0:
#             raise forms.ValidationError("A nota não pode ser negativa.")
#         return nota


# class QuizPerguntaForm(forms.ModelForm):
#     class Meta:
#         model = QuizPergunta
#         fields = ["quiz", "usuario", "pergunta"]
        


# NOTA: Arquivos em que foram comentados/removidos qualquer item relacionados às perguntas e ao quiz:
# forms.py, models.py, urls.py, admin.py, views.py
