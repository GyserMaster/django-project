from django.contrib import admin
from .models import Categoria, SubCategoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)


class SubCategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(SubCategoria, SubCategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Producto, ProductoAdmin)