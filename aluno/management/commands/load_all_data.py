from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Carrega todos os dados iniciais (cidades, cursos, etc.)"

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write(self.style.NOTICE("Iniciando o carregamento dos dados..."))

            # Chama os comandos individuais
            call_command("load_db_cidade")
            self.stdout.write(self.style.SUCCESS("Cidades carregadas com sucesso!"))

            call_command("load_db_curso")
            self.stdout.write(self.style.SUCCESS("Cursos carregados com sucesso!"))

            call_command("load_db_aluno")

            self.stdout.write(self.style.SUCCESS("Todos os dados foram carregados com sucesso!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro durante o carregamento: {e}"))
