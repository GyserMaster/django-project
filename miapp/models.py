from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titulo")
    content = models.TextField(max_length=2048)
    image = models.ImageField(blank=True, default=None, upload_to="articles")
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} - {self.public}"
    

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    created = models.DateField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.name
    