from django.db import models
from api.models import Postagem

class Comentario(models.Model):
    texto = models.TextField()
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto