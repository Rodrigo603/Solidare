from django import forms
from .models import Indicacao

class IndicacaoForm(forms.ModelForm):
    class Meta:
        model = Indicacao
        fields = ['aluno', 'empresa', 'descricao_vaga', 'recomendacao']
        widgets = {
            'descricao_vaga': forms.Textarea(attrs={'rows': 3}),
            'recomendacao': forms.Textarea(attrs={'rows': 3}),
        }
