from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=30)
    confirmacao = models.BooleanField(max_length=3)
    observacoes = models.TextField()
    convite = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.confirmacao
