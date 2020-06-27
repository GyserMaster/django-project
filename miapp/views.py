from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages

from miapp.models import Article, Category
from miapp.forms import FormArticle
from project import sql_query

import datetime


# Create your views here.
layout = """
<h1>Mi web con Django | Sergey Petrov</h1>
<hr/>
<ul>
    <li>
        <a href='/'>Inicio</a>
    </li>
    <li>
        <a href='/django'>Django</a>
    </li>
    <li>
        <a href='/pagina'>Página</a>
    </li>
    <li>
        <a href='/agnos-pares'>Años Pares</a>
    </li>
    <li>
        <a href='/contacto'>Contacto</a>
    </li>
    <li>
        <a href='/redireccionamiento'>Redireccionamiento</a>
    </li>
</ul>
<hr/>
"""
# RENDER
def index(request):
    return render(request, 'miapp/index.html', {'title':'Index'})


def hola_mundo(request):
    nombre = "Sergey Petrov"
    lenguajes = ['JavaScript', 'Python', 'DJango', 'Vue.js']
    vacio = ""
    
    return render(request, 'miapp/hola_mundo.html', {
        'title':'DJango',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'vacio':vacio,
        })



def agnos_pares(request):
    year = datetime.datetime.now().year
    max_year = int(year)+30
    agnos = []
    year_range = range(year, max_year)

    while year <= max_year:
        if year % 2 == 0:
            agnos.append(year)
            
        year += 1

    return render(request, 'miapp/agnos_pares.html', {
        'title':'Años Pares', 
        'year':datetime.datetime.now().year,
        'max_year':max_year,
        'agnos':agnos,
        'year_range':year_range,
        })

# HTTPRESPONSE
def redireccionamiento(request, rediregir=0):
    if rediregir == 1:
        return redirect('/')
    elif rediregir == 2:
        return redirect("http://google.es")
    elif rediregir == 3:
        return redirect("/contacto/nombre/apellido/")
    elif rediregir == 4:
        return redirect("contacto", nombre="Gyser", apellido="Patronus")

    return HttpResponse(layout+"<h1>Redireccionamiento</h1>")



def contacto(request, nombre="", apellido=""):
    return HttpResponse(layout+f"<h2>Contacto: {nombre} {apellido}</h2>")


def pagina(request):
    return HttpResponse(layout+"""
    <h1>Mi página</h1>
    <h3>Extensiones y configruacion de VSCode</h3>
    <p>Instalar extensiones Django y Python</p>
    <p>pip install pylint-django => configurar: settings=>
     Python › Linting: Pylint Path y añadir 'pylint_django'</p>""")


# HTTPRESPONSE - JUGANDO CON MODELOS DE ARTICULOS
def articulos(request):
    title = "Listado de articulos"
    articulos = Article.objects.filter(public=True).order_by('-pk')

    filter1 = Article.objects.filter(title="Goku", id=3)
    filter2 = Article.objects.filter(title__contains="eget")
    filter3 = Article.objects.filter(title__icontains="CuLo")
    filter4 = Article.objects.filter(title__iexact="aRTICULO UNO")
    filter5 = Article.objects.filter(id__lte=4, title__icontains="goku")
    filter6 = Article.objects.filter(id__gte=3).exclude(title__icontains="articulo").exclude(title__icontains="goku")
    query = "SELECT id FROM miapp_article WHERE title LIKE '_rticulo%'"
    #filter7 = Article.objects.raw("SELECT id FROM miapp_article WHERE title LIKE '_rticulo____'")
    filter7 = Article.objects.filter(id__in=sql_query.id_sql(query=query))  

    filter8 = Article.objects.filter(
        Q(title__contains="uno") | Q(title__contains="dos")
    )

    return render(request, 'miapp/articulos.html',{
        'title':title,
        'articulos':articulos,
        'filter1':filter1,
        'filter2':filter2,
        'filter3':filter3,
        'filter4':filter4,
        'filter5':filter5,
        'filter6':filter6,
        'filter7':filter7,
        'filter8':filter8,
    })


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return redirect('listar_articulos')
    #return HttpResponse(f"Articulo creado: {articulo.title}  contenido: {articulo.content}  creado: {articulo.created}")


def articulo(request):
    try:
        articulo = Article.objects.get(id=3, public=False)
        response = f'Articulo: {articulo.title}'
    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)


def editar_articulo(request, id, title="", content="", public=""):
    response = "Editar articulo"

    try:
        articulo = Article.objects.get(id=id)
        update = False

        if title != "":
            articulo.title = title
            update = True

        if content != "":
            articulo.content = content
            update = True
        
        if public != "":
            articulo.public = public
            update = True

        if update:
            articulo.save()
            response = f'Articulo  {articulo.id} {articulo.title} editado'
        else:
            response = f'Articulo  {articulo.id} {articulo.title} sin cambios'
        

    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)


def borrar_articulo(request, id):
    try:
        articulo = Article.objects.get(id=id)
        articulo.delete()
    except:
        print("Error al borrar")

    return redirect('listar_articulos')

# FORMULARIOS CON ARTICULOS
def save_article(request):

    if request.method == "GET":

        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']

        try:
            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            articulo.save()
            #return HttpResponse(f"Articulo creado: {articulo.title}  contenido: {articulo.content}  creado: {articulo.public}")
            return redirect('listar_articulos')

        except:
            return HttpResponse("<h2ERROR al crear el articulo</h2>")


    elif request.method == "POST" and len(request.POST['title']) >= 5 and len(request.POST['content']) >=10:

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        try:
            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            articulo.save()
            #return HttpResponse(f"Articulo creado - metodo POST funciona: {articulo.title}  contenido: {articulo.content}  creado: {articulo.public}")
            return redirect('listar_articulos')
            
        except:
            return HttpResponse("<h2ERROR al crear el articulo</h2>")

    else:
        
        return HttpResponse("<h2>No se pudo crear el articulo</h2>")
    


def create_article(request):
    title = "Formularios | create article"
    return render(request, 'miapp/create_article.html', {'title':title,})


def full_create_article(request):
    title = "Formularios | create article con formularios personalizados de DJango"
    
    if request.method == "POST":
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            datos_form = formulario.cleaned_data

            title = datos_form.get('title')
            content = datos_form['content']
            public = datos_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            # Mensajes FLASH - solo duran una sesion/refresco de pagina
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('listar_articulos')
            #return HttpResponse(articulo.title + " " + articulo.content + " " + str(articulo.public))

    else:
        formulario = FormArticle()  
    
    
    return render(request, 'miapp/full_create_article.html', {
        'form': formulario,
        'title':title,
        })