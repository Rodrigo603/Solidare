from django.urls import path
from . import views

urlpatterns = [
    path('aluno/<int:aluno_id>/boletim/', views.detalhes_aluno, name='boletim_aluno'),
    path('aluno/<int:aluno_id>/graficos/', views.historico_progresso, name='historico_progresso'),
    path('aluno/<int:aluno_id>/filtro/', views.progresso_filtrado, name='progresso_filtrado'),
]
