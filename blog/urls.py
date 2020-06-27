from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path("categoria/<int:category_id>", views.category, name="category"),
    path("erase-art/<int:articulo_id>", views.erase_art, name="borrar_articulo_blog"),
    path("detail/<int:article_id>", views.article, name="detail_articulo_blog"),
]
