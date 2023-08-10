from django.db import models
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    subtitulo = models.TextField()
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ManyToManyField('Categoria')
    
    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ('-fecha',)

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo 
    
    class Meta:
        verbose_name_plural = 'categorias'
    
    def get_absolute_url(self):
        return reverse("blog:categoria", kwargs={"pk": self.pk})