from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno, Mensagem, Doacao, Boletim, ComentarioProfessor, Indicacao, FeedbackEmpresa
from django.contrib.auth import login
from django.shortcuts import redirect



# VIEWS DE EXEMPLO

def home_view(request):
    return render(request, 'home.html')

def registrar_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

@login_required
def mensagens_view(request):
    alunos = Aluno.objects.filter(apadrinhado_por=request.user)
    return render(request, 'mensagens.html', {'alunos': alunos})

@login_required
def doacoes_view(request):
    return render(request, 'doacoes.html')

@login_required
def progresso_view(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    boletins = Boletim.objects.filter(aluno=aluno)
    comentarios = ComentarioProfessor.objects.filter(aluno=aluno)
    return render(request, 'progresso.html', {'aluno': aluno, 'boletins': boletins, 'comentarios': comentarios})

@login_required
def impacto_view(request):
    doacoes = Doacao.objects.filter(usuario=request.user)
    total = sum(d.valor for d in doacoes if d.valor)
    alunos = Aluno.objects.filter(apadrinhado_por=request.user).count()
    return render(request, 'impacto.html', {'total_doado': total, 'num_alunos': alunos})

@login_required
def banco_talentos_view(request):
    alunos = Aluno.objects.all()
    return render(request, 'banco_talentos.html', {'alunos': alunos})

@login_required
def apadrinhamento_view(request):
    return render(request, 'apadrinhamento.html')