from django.test import TestCase
from django.urls import reverse
from .models import Desempenho
from django.contrib.auth.models import User
from Aplicativo.models import Apadrinhado

class ProgressoTests(TestCase):
    def setUp(self):
        # Criar usuário colaborador para simular acesso
        self.user = User.objects.create_user(username='colab', password='12345')
        self.client.login(username='colab', password='12345')

        # Criar apadrinhado para FK
        self.aluno = Apadrinhado.objects.create(nome='Aluno Teste')

        # Criar exemplo de desempenho
        self.desempenho = Desempenho.objects.create(
            apadrinhado=self.aluno,
            mes='2025-05',
            nota=9.0,
            frequencia=95,
            comentario_professor='Ótimo desempenho'
        )

    def test_detalhes_aluno_view(self):
        url = reverse('boletim_aluno', args=[self.aluno.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ótimo desempenho')

    def test_historico_progresso_view(self):
        url = reverse('historico_progresso', args=[self.aluno.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_progresso_filtrado_view(self):
        url = reverse('progresso_filtrado', args=[self.aluno.id]) + '?filtro=nota'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
