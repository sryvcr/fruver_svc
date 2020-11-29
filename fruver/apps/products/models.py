from django.db import models
from ..providers.models import Providers


class Products(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=140)
    price = models.FloatField()
    providers = models.ForeignKey(Providers, models.DO_NOTHING, related_name='providers_id')

    class Meta:
        db_table = 'products'
