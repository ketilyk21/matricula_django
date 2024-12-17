from django import forms
from django.forms import ModelForm

from .models import Aluno, Cidade, Curso, Matricula


class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'cidade': forms.Select(attrs={'class': 'form-control' }),
        }

class AlunoFilterForm(forms.Form):
    nome = forms.CharField(max_length=150, required=False)
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(AlunoFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'data_matricula', 'data_conclusao', 'nota_final']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'data_matricula': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_conclusao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nota_final': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
        }
    
class MatriculaFilterForm(forms.Form):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(MatriculaFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'