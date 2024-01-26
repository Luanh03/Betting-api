from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display=('nome', 'email', 'cpf')
    search_fields=('nome', 'email')

admin.site.register(Usuarios, UsuariosAdmin)

