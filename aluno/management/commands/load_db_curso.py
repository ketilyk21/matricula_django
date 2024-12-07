from django.core.management.base import BaseCommand
from aluno.models import Curso  

class Command(BaseCommand):
    help = "Popula o banco de dados com cursos iniciais"

    def handle(self, *args, **kwargs):
        cursos = [
            {"nome": "Ciência da Computação"},
            {"nome": "Engenharia de Software"},
            {"nome": "Sistemas de Informação"},
            {"nome": "Análise e Desenvolvimento de Sistemas"},
            {"nome": "Redes de Computadores"},
            {"nome": "Banco de Dados"},
            {"nome": "Inteligência Artificial"},
            {"nome": "Segurança da Informação"},
            {"nome": "Gestão de TI"},
            {"nome": "Engenharia de Dados"},
        ]

        for curso in cursos:
            obj, created = Curso.objects.get_or_create(nome=curso["nome"])
            if created:
                self.stdout.write(f"Curso '{curso['nome']}' criado.")
            else:
                self.stdout.write(f"Curso '{curso['nome']}' já existe.")

        self.stdout.write(self.style.SUCCESS("Cursos populados com sucesso!"))
