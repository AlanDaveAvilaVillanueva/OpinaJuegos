from django.contrib import admin
from .models import *


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_lanzamiento')  # columnas visibles en la lista
    search_fields = ('titulo',)                     # agrega buscador
    list_filter = ('fecha_lanzamiento',)            # filtros laterales


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'juego', 'puntaje', 'fecha')
    list_filter = ('puntaje', 'fecha')
    search_fields = ('comentario', 'usuario__nombre', 'juego__titulo')
