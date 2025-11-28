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


# ---------------------------------------------------------
# MODELO ANTIGO (mantido por causa do admin)
# ---------------------------------------------------------
class Mensagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    apelido = models.CharField(max_length=50)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    pai = models.ForeignKey('self', null=True, blank=True, related_name='respostas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.apelido} - {self.texto[:30]}"


# ---------------------------------------------------------
# NOVO SISTEMA DE CHAT (usado no front)
# ---------------------------------------------------------
class ChatMensagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    apelido = models.CharField(max_length=50)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    pai = models.ForeignKey('self', null=True, blank=True, related_name='respostas', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.apelido}: {self.texto[:40]}"

# Temporário    
class Denuncia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    apelido = models.CharField(max_length=50)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Denúncia de {self.apelido}"

