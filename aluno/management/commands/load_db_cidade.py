from django.core.management.base import BaseCommand
from aluno.models import Cidade  # Substitua 'seu_app' pelo nome do seu aplicativo

class Command(BaseCommand):
    help = "Popula o banco de dados com cidades iniciais"

    def handle(self, *args, **kwargs):
        cidades = [
            {"nome": "Natal", "sigla_estado": "RN"},
            {"nome": "Mossoró", "sigla_estado": "RN"},
            {"nome": "João Pessoa", "sigla_estado": "PB"},
            {"nome": "Recife", "sigla_estado": "PE"},
            {"nome": "Fortaleza", "sigla_estado": "CE"},
            {"nome": "Salvador", "sigla_estado": "BA"},
            {"nome": "São Paulo", "sigla_estado": "SP"},
            {"nome": "Rio de Janeiro", "sigla_estado": "RJ"},
            {"nome": "Belo Horizonte", "sigla_estado": "MG"},
            {"nome": "Curitiba", "sigla_estado": "PR"},
        ]

        for cidade in cidades:
            obj, created = Cidade.objects.get_or_create(
                nome=cidade["nome"], sigla_estado=cidade["sigla_estado"]
            )
            if created:
                self.stdout.write(f"Cidade {cidade['nome']} - {cidade['sigla_estado']} criada.")
            else:
                self.stdout.write(f"Cidade {cidade['nome']} - {cidade['sigla_estado']} já existe.")

        self.stdout.write(self.style.SUCCESS("Cidades populadas com sucesso!"))
