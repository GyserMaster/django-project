from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name='main_index'),
    path('about/', views.about, name='main_about'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
