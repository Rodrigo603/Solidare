from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import Aluno, Mensagem, Doacao, Boletim, ComentarioProfessor, Profile
from django.db import IntegrityError

def home_view(request):
    return render(request, 'home.html')

def registrar_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'registration/registrar.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return render(request, 'registration/registrar.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe uma conta com este e-mail.")
            return render(request, 'registration/registrar.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('home')
        except IntegrityError:
            messages.error(request, "Erro ao criar o usuário.")
    
    return render(request, 'registration/registrar.html')

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

@login_required
def perfil_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    is_editing = request.GET.get('editar') == '1'

    if request.method == 'POST':
        bio = request.POST.get('bio')
        foto = request.FILES.get('foto')
        email = request.POST.get('email')

        request.user.email = email
        request.user.save()

        if bio:
            profile.bio = bio
        if foto:
            profile.foto = foto
        profile.save()

        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('perfil')

    return render(request, 'perfil.html', {
        'email': request.user.email,
        'usuario': request.user.usuario,
        'foto': profile.foto.url if profile.foto else None,
        'profile': profile,
        'is_editing': is_editing,
    })
