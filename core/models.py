from django.db import models

class ClientToken(models.Model):
    client_id = models.CharField('Client ID', max_length=100)
    client_secret = models.CharField('Client Secret', max_length=100)

class Playlist(models.Model):
    id = models.CharField('ID', max_length=100, primary_key=True, auto_created=False)
    nome = models.CharField('Nome', max_length=100, null=True)
    capa = models.URLField('Capa', max_length=640, null=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False, null=True)

    def __str__(self):
        return f'{self.id}'

class AccessTokenScoped(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    access_token_scoped = models.CharField('Acess Token Scoped', max_length=300)

    def __str__(self):
        return f'{self.access_token_scoped}'