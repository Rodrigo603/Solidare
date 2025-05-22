from django.contrib import admin

# Register your models here.
from .models import Desempenho, HistoricoProgresso

admin.site.register(Desempenho)
admin.site.register(HistoricoProgresso)
