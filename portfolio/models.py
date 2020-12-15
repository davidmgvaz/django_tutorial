from django.db import models
from django.urls import reverse


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projeto/%Y/')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('projeto', kwargs={'pk': self.id})


class Comentario(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    comentario = models.TextField()

    def __str__(self):
        return f'{self.projeto}: {self.nome}'
