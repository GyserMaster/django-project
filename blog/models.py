from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nombre")
    description = models.TextField(max_length=2048, verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titulo")
    content = RichTextField(max_length=4096, verbose_name="Contenido")
    image = models.ImageField(blank=True, default=None, upload_to="articles")
    public = models.BooleanField(default=True)
    # MODELO RELACIONAL
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True)
    # ----
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ["-created"]

    def __str__(self):
        return self.title