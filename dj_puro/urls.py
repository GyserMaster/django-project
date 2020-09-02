from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categoria_list, name="categoria_list"),
    path('categorias/<int:pk>', views.categoria_detail, name="categoria_detail")
]

