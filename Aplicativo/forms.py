from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')  # Adiciona o campo manualmente

    class Meta:
        model = Profile
        fields = ['foto', 'nome', 'descricao']
        labels = {
            'foto': 'Foto de Perfil',
            'nome': 'Nome',
            'descricao': 'Descrição',
        }


    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile
