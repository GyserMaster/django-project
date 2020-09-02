from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .permissions import IsOwner
from .models import Producto, SubCategoria, Categoria
from .serializers import (ProductoSerializer, SubCategoriaSerializer, CategoriaSerializer, 
UserSerializer)


class UserLogin(APIView):
    permission_classes = ()
 
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    authentication_classes = () # esto sobreescribe el REST_FRAMEWORK de settings.py
    permission_classes = () # esto sobreescribe el REST_FRAMEWORK de settings.py 
    serializer_class = UserSerializer


# --- PRODUCTO ---
# GET POST
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()[:4]
    serializer_class = ProductoSerializer
 
# GET DELETE 
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = ([IsAuthenticated, IsOwner])

# ALL HTTP REQUESTS METHODS
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# --- SUBCATEGORIA ---

# GET POST
class SubCategoriaDetalle(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset

    serializer_class = SubCategoriaSerializer

# GET POST
class SubCategoriaList(generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer

class SubCategoriaAdd(APIView):
    def post(self, request, pk):
        descripcion = request.data.get("descripcion")
        data = {"categoria":pk, "descripcion":descripcion}
        serializer = SubCategoriaSerializer(data=data)

        if serializer.is_valid():
            subcategoria = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# --- CATEGORIA ---
# GET POST
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# GET DELETE
class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer





# # POST
# class SubCategoriaSave(generics.CreateAPIView):
#     serializer_class = SubCategoriaSerializer


# # POST
# class CategoriaSave(generics.CreateAPIView):
#     serializer_class = CategoriaSerializer


# class ProductoList(APIView):

#     def get(self, request):
#         productos = Producto.objects.all()[:4]
#         data = ProductoSerializer(productos, many=True).data

#         return Response(data)


# class ProductoDetalle(APIView):

#     def get(self, request, pk):
#         producto = get_object_or_404(Producto, pk=pk)
#         data = ProductoSerializer(producto).data

#         return Response(data)

