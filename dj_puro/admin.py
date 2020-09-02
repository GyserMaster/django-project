from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin)