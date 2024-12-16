"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from aluno.views import (
    aluno_criar,
    aluno_editar,
    aluno_listar,
    aluno_remover,
    index,
    matricula_criar,
    matricula_editar,
    matricula_remover,
    matriculas_listar,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('aluno/',aluno_criar,name='aluno_criar'),
    path('aluno/editar/<int:id>/',aluno_editar, name='aluno_editar'),
    path('aluno/remover/<int:id>/',aluno_remover,name='aluno_remover'),
    path('aluno/listar',aluno_listar,name='aluno_listar'),
    path('matricula/listar',matriculas_listar,name='matricula_listar'),
    path('matricula/criar',matricula_criar,name='matricula_criar'),
    path('matricula/editar/<int:id>/',matricula_editar,name='matricula_editar'),
    path('matricula/remover/<int:id>/',matricula_remover,name='matricula_remover'),
]


