from django.shortcuts import render, get_object_or_404
from Aplicativo.models import Apadrinhado
from .models import Desempenho

def detalhes_aluno(request, aluno_id):
    """Cenário 1: Consulta ao boletim do aluno"""
    aluno = get_object_or_404(Apadrinhado, id=aluno_id)
    desempenho = Desempenho.objects.filter(apadrinhado=aluno).order_by('mes')
    return render(request, 'progresso/detalhes_aluno.html', {
        'aluno': aluno,
        'desempenho': desempenho
    })

def historico_progresso(request, aluno_id):
    """Cenário 2: Relatórios de progresso periódicos - gráficos e estatísticas"""
    aluno = get_object_or_404(Apadrinhado, id=aluno_id)
    desempenho = Desempenho.objects.filter(apadrinhado=aluno).order_by('mes')

    meses = [d.mes for d in desempenho]
    notas = [float(d.nota) for d in desempenho]
    frequencias = [float(d.frequencia) for d in desempenho]

    context = {
        'aluno': aluno,
        'meses': meses,
        'notas': notas,
        'frequencias': frequencias,
    }
    return render(request, 'progresso/historico_progresso.html', context)

def progresso_filtrado(request, aluno_id):
    """Cenário 3: Relatórios personalizados com filtros via GET"""
    aluno = get_object_or_404(Apadrinhado, id=aluno_id)
    filtro = request.GET.get('filtro', 'nota')  # 'nota', 'frequencia' ou 'comentario'

    desempenho = Desempenho.objects.filter(apadrinhado=aluno).order_by('mes')

    if filtro == 'nota':
        dados = [(d.mes, d.nota) for d in desempenho]
    elif filtro == 'frequencia':
        dados = [(d.mes, d.frequencia) for d in desempenho]
    elif filtro == 'comentario':
        dados = [(d.mes, d.comentario_professor) for d in desempenho]
    else:
        dados = []

    return render(request, 'progresso/progresso_filtrado.html', {
        'aluno': aluno,
        'dados': dados,
        'filtro': filtro,
    })
