from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'providers_id', )
        read_only_fields = ('id', 'name', 'price', 'providers_id', )
