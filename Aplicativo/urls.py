from django.urls import path
from .views import mensagens_view, doacoes_view, progresso_view, impacto_view, banco_talentos_view

urlpatterns = [
    path('mensagens/', mensagens_view, name='mensagens'),
    path('doacoes/', doacoes_view, name='doacoes'),
    path('progresso/<int:aluno_id>/', progresso_view, name='progresso'),
    path('impacto/', impacto_view, name='impacto'),
    path('talentos/', banco_talentos_view, name='banco_talentos'),
]
