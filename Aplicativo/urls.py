from django.urls import path
from .views import home_view, mensagens_view, doacoes_view, progresso_view
from .views import impacto_view, banco_talentos_view, registrar_view, apadrinhamento_view

urlpatterns = [
    path('', home_view, name='home'),
    path('registrar/', registrar_view, name='registrar'),
    path('mensagens/', mensagens_view, name='mensagens'),
    path('doacoes/', doacoes_view, name='doacoes'),
    path('progresso/<int:aluno_id>/', progresso_view, name='progresso'),
    path('impacto/', impacto_view, name='impacto'),
    path('talentos/', banco_talentos_view, name='banco_talentos'),
    path('apadrinhar/', apadrinhamento_view, name='apadrinhar')

]
