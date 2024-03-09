from django.db import models
from django.utils import timezone
# Create your models here.

LISTA_CATEGORIA = (
    ('acao', 'Ação'),
    ('animacao', 'Animação'),
    ('comedia', 'Comedia'),
    ('ficcao', 'Ficção científica'),
    ('suspense', 'Suspense'),
    ('terror', 'Terror'),
    ('drama', 'Drama'),
    ('romance', 'Romance'),
    ('documentario', 'Documentario'),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    def get_categoria_display(self):
        for categoria, nome in LISTA_CATEGORIA:
            if categoria == self.categoria:
                return nome
        return None
    
class Video(models.Model):
    filme = models.ForeignKey("Filme", related_name='video', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    video = models.URLField()
    trailer = models.URLField()

    def __str__(self):
        return self.titulo