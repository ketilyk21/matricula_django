from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm,AlunoFilterForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Curso, Cidade
from .forms import AlunoForm, AlunoFilterForm
from django.core.paginator import Paginator

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'aluno/form.html',{'form':form})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {'form': form})
# views.py


def aluno_listar(request):
    alunos = Aluno.objects.all()
    form_filtro = AlunoFilterForm(request.GET or None)

    if form_filtro.is_valid():
        # Pega os valores dos filtros   
        nome = form_filtro.cleaned_data.get('nome')
        cidade = form_filtro.cleaned_data.get('cidade')
        curso = form_filtro.cleaned_data.get('curso')
        # Aplica os filtros no queryset        
        if nome:
            alunos = alunos.filter(nome_aluno__icontains=nome)
        if cidade:
            alunos = alunos.filter(cidade=cidade)
        if curso:
            alunos = alunos.filter(curso=curso)

    # Configura a paginação usando get_page()
    paginator = Paginator(alunos, 10)  # Mostra 10 alunos por página
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)  # Evita exceções ao lidar com páginas inválidas

    context = {
        'page_obj': page_obj,  # Passa 'page_obj' para o template
        'form_filtro': form_filtro
    }

    return render(request, "aluno/alunos.html", context)




def index(request):
    total_alunos = Aluno.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html",context)

