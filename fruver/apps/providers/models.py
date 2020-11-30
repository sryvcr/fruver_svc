from django.db import models


class Providers(models.Model):
    document_id = models.CharField(primary_key=True, max_length=30, unique=True)
    name = models.CharField(max_length=140)

    class Meta:
        db_table = 'providers'
        ordering = ['name']
