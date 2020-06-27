"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

#from miapp import views
import miapp.views
import mainapp.views
import pages.views


urlpatterns = [
    path('admin/', admin.site.urls),

    # BLOG
    path('', include("blog.urls")),

    # MAINAPP
    path('', include("mainapp.urls")),

    # PAGEAPP
    path('', include("pages.urls")),

    # MIAPP
    path('', miapp.views.index, name='index'),
    path('django/', miapp.views.hola_mundo, name='django'),

    path('pagina/', miapp.views.pagina, name='pagina'),
    path('agnos-pares/', miapp.views.agnos_pares, name='agnos_pares'),

        # CONTACTO
    path('contacto/', miapp.views.contacto, name='contacto'),
    path('contacto/<str:nombre>/', miapp.views.contacto, name='contacto'),
    path('contacto/<str:nombre>/<str:apellido>/', miapp.views.contacto, name='contacto'),

        # REDIRECCIONAMIENTO
    path('redireccionamiento/', miapp.views.redireccionamiento, name='redir'),
    path('redireccionamiento/<int:rediregir>', miapp.views.redireccionamiento, name='redir'),

        # Jugando con modelos
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', miapp.views.crear_articulo, name="crear_articulo"),
    path('articulo/', miapp.views.articulo, name="articulo"),
    path('editar-articulo/<int:id>/', miapp.views.editar_articulo, name="editar_articulo"),
    path('editar-articulo/<int:id>/<str:title>/', miapp.views.editar_articulo, name="editar_articulo"),
    path('editar-articulo/<int:id>/<str:title>/<str:content>/', miapp.views.editar_articulo, name="editar_articulo"),
    path('editar-articulo/<int:id>/<str:title>/<str:content>/<str:public>/', miapp.views.editar_articulo, name="editar_articulo"),
    path('articulos/', miapp.views.articulos, name="listar_articulos"),
    path('borrar-articulo/<int:id>/', miapp.views.borrar_articulo, name="borrar_articulo"),
    path('save-article/', miapp.views.save_article, name="save"),
    path('create-article/', miapp.views.create_article, name="create"),
    path('full-create-article/', miapp.views.full_create_article, name="full_create"),
]

# Configuracion de para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
