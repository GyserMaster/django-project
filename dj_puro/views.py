from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Categoria

def categoria_list(request):
    MAX_OBJECTS = 5
    categorias = Categoria.objects.all()[:MAX_OBJECTS]
    print(vars(categorias))
    data = {
        "results": list(categorias.values("id", "descripcion", "activo"))
    }

    response = JsonResponse(data)
    return response
    #return render(request, response)

def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    data = {
        "results":{
            "descripcion":categoria.descripcion,
            "activo":categoria.activo,
            "created":categoria.created,
            "updated":categoria.updated
        }
    }
    response = JsonResponse(data)
    return response
