from django.db import models

class Usuario(models.Model):
    nome  = models.CharField(max_length=100, verbose_name="Nome do alimento")
    cpf = models.CharField(max_length=100, verbose_name="É apropriado para") # ------------------------ (como ligar mais de um animal nessa parte dos apropriados)
    senha = models.CharField(max_length=100, verbose_name="É inapropriado para")
    email = models.CharField(max_length=100, verbose_name="É inapropriado para") # --------------------- ()
    idade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Açúcares totais (100g)")
    
    def __str__(self):
        return self.nome
    
# --------------------------------------------------------------------------------------------------------------------------   
    
class Administrador(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da doença")
    setor = models.CharField(max_length=100, verbose_name="Sintomas")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
# --------------------------------------------------------------------------------------------------------------------------
    
class Acesso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dataHora = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.usuario.nome} entrou em {self.dataHora}"
    
# --------------------------------------------------------------------------------------------------------------------------
    
class Mensagem(models.Model):
    mensagem = models.TextField()
    dataHora = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alimento} - {self.quantidade_diaria}"
# --------------------------------------------------------------------------------------------------------------------------
    
class Denuncia(models.Model):
    mensagem = models.CharField(max_length=45)
    data_hora = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Denúncia {self.id} - {self.mensagem}"

# --------------------------------------------------------------------------------------------------------------------------   
    
class Pergunta(models.Model):
    pergunta = models.CharField(max_length=45)
    nivel = models.IntegerField()

    def __str__(self):
        return self.pergunta
    
# --------------------------------------------------------------------------------------------------------------------------
    
class Quiz(models.Model):
    nota = models.FloatField()
    data_hora = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perguntas = models.ManyToManyField(Pergunta, through="QuizPergunta")

    def __str__(self):
        return f"Quiz {self.id} - Nota: {self.nota}"
    
# --------------------------------------------------------------------------------------------------------------------------
    
class QuizPergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Quiz {self.quiz.id} - Pergunta {self.pergunta.id}"
    



# from django.db import models

# class Cidade(models.Model):
#     nome = models.CharField(max_length=100)
#     uf = models.CharField(max_length=2)

#     def __str__(self):
#         return f"{self.nome} - {self.uf}"

# # --------------------------------------------------------------------------------------------------------------------------

# class Alimento(models.Model):
#     alimento  = models.CharField(max_length=100, verbose_name="Nome do alimento")
#     apropriado = models.CharField(max_length=100, verbose_name="É apropriado para") # ------------------------ (como ligar mais de um animal nessa parte dos apropriados)
#     inapropriado = models.CharField(max_length=100, verbose_name="É inapropriado para")
#     valor_energetico = models.DecimalField(verbose_name="Valor energético (Cal)") # --------------------- ()
#     acucares_totais = models.DecimalField(verbose_name="Açúcares totais (100g)")
#     carboidratoss = models.DecimalField(verbose_name="Carboidratos (100g)")
#     proteinas = models.DecimalField(verbose_name="Proteínas (100g)")
#     gorduras_totais = models.DecimalField(verbose_name="Gorduras totais (100g)") 
#     fibras = models.DecimalField(verbose_name="Proteínas (100g)")
#     sodio = models.DecimalField(verbose_name="Sódio (100g)")

#     def __str__(self):
#         return self.alimento
# # --------------------------------------------------------------------------------------------------------------------------   
# class Doenca(models.Model):
#     nome = models.CharField(max_length=100, verbose_name="Nome popular")
#     nome_cientifico = models.CharField(max_length=100, verbose_name="Nome científico")
#     sintomas = models.CharField(max_length=100, verbose_name="Sintomas")
#     possiveis_causas = models.CharField(max_length=100, verbose_name="Possíveis causas da doença")

#     def __str__(self):
#         return self.nome
# # --------------------------------------------------------------------------------------------------------------------------
# class Animal(models.Model):
#     animal = models.CharField(max_length=100, verbose_name="Animal")
#     raca = models.CharField(max_length=100, verbose_name="Raça")
#     nome_cientifico = models.CharField(max_length=100, verbose_name="Nome científico")
#     porte = models.CharField(max_length=14, verbose_name="Porte (pequeno, médio ou grande)")
#     expectativa_vida = models.CharField(max_length=100, verbose_name="Expectativa média de vida")
#     alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.animal
# # --------------------------------------------------------------------------------------------------------------------------
# class Dieta(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
#     alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
#     quantidade_diaria = models.IntegerField(verbose_name="quantidade diária (g)")

#     def __str__(self):
#         return self.nome # ---------------------
# # --------------------------------------------------------------------------------------------------------------------------
# class Especificacoes(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
#     alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
# # --------------------------------------------------------------------------------------------------------------------------   
# class Sugestao(models.Model):
#     sugestao = models.TextField()

#     def __str__(self):
#         return self.sugestao
# # --------------------------------------------------------------------------------------------------------------------------
# class questionario(models.Model):
#     animal = models.CharField(max_length=100, verbose_name="Nome do animal")
#     raça = models.CharField(max_length=100, verbose_name="Nome do animal")
#     porte = models.CharField(max_length=100, verbose_name="Nome do animal")
#     peso = models.DecimalField(verbose_name="Gorduras totais (100g)")
#     idade = models.IntegerField(verbose_name="quantidade diária (g)")
#     possui_doenca = models.CharField(max_length=100, verbose_name="Nome do animal")
#     alergia = models.CharField(max_length=100, verbose_name="Nome do animal")

#     def __str__(self):
#         return self.nome
# # --------------------------------------------------------------------------------------------------------------------------   



