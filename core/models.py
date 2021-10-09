from django.db import models
class AccessTokenScoped(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    access_token_scoped = models.CharField('Acess Token Scoped', max_length=300)

    def __str__(self):
        return f'{self.access_token_scoped}'