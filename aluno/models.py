from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + " - " + self.sigla_estado 

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome 

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.nome_aluno} - {self.curso.nome}"
