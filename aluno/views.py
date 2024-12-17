from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoFilterForm, AlunoForm, MatriculaFilterForm, MatriculaForm
from .models import Aluno, Cidade, Curso, Matricula


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
    total_matriculas = Matricula.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cursos' : total_curso,
        'total_matriculas': total_matriculas
    }
    return render(request, "aluno/index.html",context)

def matriculas_listar(request):
    matriculas = Matricula.objects.all()

    form_filtro = MatriculaFilterForm(request.GET or None)

    if form_filtro.is_valid():
        # Pega os valores dos filtros   
        aluno = form_filtro.cleaned_data.get('aluno')
        curso = form_filtro.cleaned_data.get('curso')
        # Aplica os filtros no queryset        
        if aluno:
            matriculas = matriculas.filter(aluno=aluno)
        if curso:
            matriculas = matriculas.filter(curso=curso)

    paginator = Paginator(matriculas, 10) 
    page = request.GET.get('page')
    page_obj = paginator.get_page(page) 

    context = {
        'page_obj': page_obj, 
        'form_filtro': form_filtro
    }
    return render(request, 'aluno/matriculas.html', context)

def matricula_editar(request,id):
    matricula = get_object_or_404(Matricula,id=id)
   
    if request.method == 'POST':
        form = MatriculaForm(request.POST,instance=matricula)

        if form.is_valid():
            form.save()
            return redirect('matricula_listar')
    else:
        form = MatriculaForm(instance=matricula)

    return render(request,'aluno/form_matricula.html',{'form':form})


def matricula_remover(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('matricula_listar') 


def matricula_criar(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matricula_listar')
            form = MatriculaForm()
    else:
        form = MatriculaForm()

    return render(request, "aluno/form_matricula.html", {'form': form})
