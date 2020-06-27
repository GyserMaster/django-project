from django.contrib import admin
from .models import Page


# Configuraicon extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created')
    ordering = ('-created',)





# Register your models here.
admin.site.register(Page, PageAdmin)

'''
title = "Proyectorl Djangorl"
subtitle = "Panel de gestionrl"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
'''