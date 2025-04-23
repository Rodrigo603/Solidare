from django.urls import path
from .views import editar_apadrinhados, excluir_apadrinhado, home_view, mensagens_view, doacoes_view, progresso_view
from .views import impacto_view, banco_talentos_view, registrar_view, apadrinhamento_view,logout_view
from .views import perfil_view, registrar_apadrinhado_view,login_view,lista_apadrinhados,editar_apadrinhados

urlpatterns = [
    path('', home_view, name='home'),
    path('registrar/', registrar_view, name='registrar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('mensagens/', mensagens_view, name='mensagens'),
    path('doacoes/', doacoes_view, name='doacoes'),
    path('progresso/<int:aluno_id>/', progresso_view, name='progresso'),
    path('impacto/', impacto_view, name='impacto'),
    path('talentos/', banco_talentos_view, name='banco_talentos'),
    path('apadrinhar/', apadrinhamento_view, name='apadrinhar'),
    path('perfil/', perfil_view, name='perfil'),
    path('registrar/apadrinhado/', registrar_apadrinhado_view, name='registrar_apadrinhado'),
    path('apadrinhados/',lista_apadrinhados, name='lista_apadrinhados'),
    path('apadrinhados/editar<int:apadrinhado_id>/editar', editar_apadrinhados, name='editar_apadrinhado'),
    path('apadrinhados/excluir<int:apadrinhado_id>/excluir', excluir_apadrinhado, name='excluir_apadrinhado'),
]
