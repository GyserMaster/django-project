from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import  include_docs_urls

from .viewsapi import (ProductoList, ProductoDetalle, ProductoViewSet,
SubCategoriaList, SubCategoriaDetalle, SubCategoriaAdd,
CategoriaList, CategoriaDetalle,
UserCreate, UserLogin)


router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')

schema_view = get_swagger_view(title="RestFul Api DRF Doc")
urlpatterns = [
    path('newuser/', UserCreate.as_view(), name="new_user"),
    path('login/', UserLogin.as_view(), name="login_user"),
    path('login-drf/', views.obtain_auth_token, name="login_drf"),

    path('producto/', ProductoList.as_view(), name="producto_list"),
    path('producto/<int:pk>/', ProductoDetalle.as_view(), name="producto_detail"),
    path('subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list' ),
    path('categorias/<int:pk>/subcategorias/', SubCategoriaDetalle.as_view(), name='subcategoria_detalle' ),
    path('categorias/<int:pk>/subcategorias/add/', SubCategoriaAdd.as_view(), name='subcategoria_add' ),
    path('categorias/', CategoriaList.as_view(), name='categoria_list' ),
    path('categorias/<int:pk>/', CategoriaDetalle.as_view(), name='categoria_detalle' ),
    
    #categorias/pk/subcategorias/   #Para mostrar todas las sub categorías de una categoría
    #categorias/pk/subcategorias/pk  #Para devolver una sub categoría de una categoría
    
    path('swagger-docs/', schema_view, name="swagger_doc"),
    path('coreapi-docs/', include_docs_urls(title="Documentacion CoreAPI"), name="coreapi_doc"),

]

urlpatterns += router.urls