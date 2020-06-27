from blog.models import Category, Article

# VARIABLES GLOBALES
def get_categories(request):

    ids = Article.objects.filter(public=True).values_list("categories", flat=True)
    categorys = Category.objects.filter(id__in=ids).values_list("id", "name")

    return {
        "categorys":categorys,
        "ids":ids
    }