from django import forms
from .models import Usuario, Administrador, Acesso, Mensagem, Denuncia, Pergunta, Quiz, QuizPergunta


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "cpf", "senha", "email", "data_nasc"]

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("O CPF deve conter apenas números e ter 11 dígitos.")
        return cpf

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email


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
    consentimento = forms.BooleanField(required=True, label="Concordo que as informações serão usadas para investigação")

    class Meta:
        model = Denuncia
        fields = ['categoria', 'descricao', 'email', 'anexo', 'consentimento']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva o ocorrido com o máximo de detalhes.'}),
        }

    def clean_descricao(self):
        desc = self.cleaned_data['descricao'].strip()
        if len(desc) < 10:
            raise forms.ValidationError("A descrição deve conter pelo menos 10 caracteres.")
        return desc


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ["pergunta", "nivel"]

    def clean_nivel(self):
        nivel = self.cleaned_data["nivel"]
        if nivel < 1:
            raise forms.ValidationError("O nível deve ser maior que 0.")
        return nivel


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["nota", "data_hora", "usuario", "perguntas"]

    def clean_nota(self):
        nota = self.cleaned_data["nota"]
        if nota < 0:
            raise forms.ValidationError("A nota não pode ser negativa.")
        return nota


class QuizPerguntaForm(forms.ModelForm):
    class Meta:
        model = QuizPergunta
        fields = ["quiz", "usuario", "pergunta"]
