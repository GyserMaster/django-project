from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def list(request):

    #Sacar art
    articles = Article.objects.all()

    # Paginar art
    paginator = Paginator(articles, 2)

    #Recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, "blog/list.html", {
        "title": "Articulos",
        "articulos":page_articles,
    })

@login_required(login_url="login")
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, "blog/category.html",{
        "category": category,
        "articulos": articles,
    })


@login_required(login_url="login")
def erase_art(request, articulo_id):
    try:
        articulo = Article.objects.get(id=articulo_id)
        articulo.delete()
    except:
        print("Error al borrar")

    return redirect('list')


@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, "blog/detail.html", {
        "article":article,
    })