from django.urls import path
from . import views

urlpatterns = [
    path('page/<str:slug>', views.page, name='page'),
]
