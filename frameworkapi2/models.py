from django.db import models

class JsonPlaceholder(models.Model):
    """ Classe responsavel por modelar os dados da api """
    userId = models.CharField(max_length=50)
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

