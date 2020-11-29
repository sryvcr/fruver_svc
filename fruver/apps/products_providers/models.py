from django.db import models


class Providers(models.Model):
    document_id = models.CharField(primary_key=True, max_length=30, unique=True)
    name = models.CharField(max_length=140)

    class Meta:
        db_table = 'providers'


class Products(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=140)
    price = models.FloatField()
    providers_id = models.ForeignKey(Providers,  models.DO_NOTHING, related_name='providers_id')

    class Meta:
        db_table = 'products'
