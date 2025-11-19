from django.db import models
import uuid
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=45, unique=True)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=100, unique=True)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome


class Administrador(models.Model):
    setor = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Administrador {self.id} - {self.setor}"


class Acesso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.usuario.nome} entrou em {self.data_hora}"


class Mensagem(models.Model):
    mensagem = models.TextField()
    data_hora = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensagem


def upload_path(instance, filename):
    return f"denuncias/{instance.id}/{filename}"

class Denuncia(models.Model):
    CATEGORIAS = [
        ('golpe_pix', 'Golpe do Pix'),
        ('phishing', 'Phishing / Falso Link'),
        ('falso_suporte', 'Falso Suporte Técnico'),
        ('roubo_conta', 'Roubo de Conta / Clonagem'),
        ('site_falso', 'Site Falso / Loja Fake'),
        ('falso_premio', 'Golpe do Prêmio / Sorteio Falso'),
        ('engenharia_social', 'Engenharia Social'),
        ('outro', 'Outro'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='outro')
    descricao = models.TextField(default='')
    email = models.EmailField(blank=True, null=True)
    anexo = models.FileField(upload_to=upload_path, blank=True, null=True)
    status = models.CharField(max_length=20, default='pendente')

    def __str__(self):
        return f"{self.id} - {self.get_categoria_display()}"


    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=45)
    nivel = models.IntegerField()

    def __str__(self):
        return self.pergunta


class Quiz(models.Model):
    nota = models.FloatField()
    data_hora = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perguntas = models.ManyToManyField(Pergunta, through="QuizPergunta")

    def __str__(self):
        return f"Quiz {self.id} - Nota: {self.nota}"


class QuizPergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Quiz {self.quiz.id} - Pergunta {self.pergunta.id}"
    