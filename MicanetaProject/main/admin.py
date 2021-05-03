from django.contrib import admin
from . import models


@admin.register(models.Equipo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id', 'ubicacion', 'slug',
                    'creador', 'ubicacion')
    prepopulated_fields = {'slug': ('nombre',), }
