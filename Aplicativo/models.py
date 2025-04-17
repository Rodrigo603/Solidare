from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# MODELS

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

@receiver(post_save, sender=User)
def criar_ou_atualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='alunos_fotos/')
    apadrinhado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apadrinhados')

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    texto = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    entregue = models.BooleanField(default=False)

class Doacao(models.Model):
    TIPO_CHOICES = [('Financeira', 'Financeira'), ('Material', 'Material')]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.CharField(max_length=255, blank=True)
    comprovante = models.FileField(upload_to='comprovantes/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.CharField(max_length=50)
    nota = models.FloatField()
    frequencia = models.IntegerField()

class ComentarioProfessor(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateField(auto_now_add=True)

class Indicacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)
    descricao_vaga = models.TextField()
    recomendacao = models.TextField()
    status = models.CharField(max_length=30, default='Pendente')

class FeedbackEmpresa(models.Model):
    indicacao = models.OneToOneField(Indicacao, on_delete=models.CASCADE)
    feedback = models.TextField()
    data = models.DateField(auto_now_add=True)