from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('name', 'created')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("user", "created", "updated")
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user','public', 'created')
    list_filter = ('public', 'user__username', 'categories__name', 'created')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)