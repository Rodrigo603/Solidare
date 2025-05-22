from django.db import models

class Desempenho(models.Model):
    apadrinhado = models.ForeignKey('Aplicativo.Apadrinhado', on_delete=models.CASCADE)
    mes = models.CharField(max_length=20)  
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    frequencia = models.DecimalField(max_digits=5, decimal_places=2)  
    comentario_professor = models.TextField(blank=True)

    def __str__(self):
        return f"{self.apadrinhado.nome} - {self.mes}"
