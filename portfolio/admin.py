from django.contrib import admin

from .models import Projeto, Comentario


class ComentarioAdmin(admin.TabularInline):
    model = Comentario
    fields = ['nome', 'comentario']


class ProjetoAdmin(admin.ModelAdmin):
    inlines = [ComentarioAdmin]


admin.site.register(Projeto, ProjetoAdmin)
