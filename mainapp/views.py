from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from project import sql_query
from .forms import RegisterForm

import datetime
# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio'
    })

@login_required(login_url="login")
def about(request):
    return render(request, "mainapp/about.html", {
        'title': "About me",
    })


def register_page(request):

    if request.user.is_authenticated:
        return redirect(main_index)

    #formulario_de_registro = UserCreationForm()
    formulario_de_registro = RegisterForm()

    if request.method == "POST":
        print(request.POST) 
        #formulario_de_registro = UserCreationForm(request.POST)
        formulario_de_registro = RegisterForm(request.POST)

        if formulario_de_registro.is_valid():
            formulario_de_registro.save()

            messages.success(request, "Usuario registrado correctamente")

            return redirect("login")

    return render(request, "mainapp/register.html", {
        "title": "Registro",
        "register_form":formulario_de_registro,
    })


def login_page(request):

    if request.user.is_authenticated:
        return redirect("main_index")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logeado correctamente")
            
            return redirect("main_index")
        
        else:
            messages.warning(request, "No se pudo logear, datos incorrectos :(")
            

    return render(request, 'mainapp/login.html', {
        'title':'Login',
    })


def logout_page(request):

    logout(request)

    return redirect("main_index")