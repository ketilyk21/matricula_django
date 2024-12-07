from django.core.management.base import BaseCommand
from aluno.models import Aluno, Cidade, Curso  # Substitua 'aluno' pelo nome do seu app
from faker import Faker
import random

class Command(BaseCommand):
    help = "Popula o banco de dados com 20 alunos fictícios"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Obtém todas as cidades e cursos previamente carregados
        cidades = list(Cidade.objects.all())
        cursos = list(Curso.objects.all())

        if not cidades or not cursos:
            self.stdout.write(self.style.ERROR("Certifique-se de que cidades e cursos estão carregados antes de executar este comando."))
            return

        # Cria 20 alunos fictícios
        for _ in range(20):
            nome_aluno = fake.name()
            endereco = fake.address()
            email = fake.email()
            cidade = random.choice(cidades)
            curso = random.choice(cursos)

            # Cria o aluno no banco de dados
            Aluno.objects.create(
                nome_aluno=nome_aluno,
                endereco=endereco,
                email=email,
                cidade=cidade,
                curso=curso
            )

        self.stdout.write(self.style.SUCCESS("20 alunos fictícios foram criados com sucesso!"))
