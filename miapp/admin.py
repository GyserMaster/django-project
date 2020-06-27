from django.contrib import admin
from .models import Article, Category


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)




# Configurar el titulo de panel de administracion
admin.site.site_header = "Master DJango"
admin.site.index_title = "Panel administrativo"
admin.site.site_title = "Panel de Administracion"