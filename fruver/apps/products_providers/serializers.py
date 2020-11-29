from rest_framework import serializers
from .models import (
    Providers,
)


class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = ('document_id', 'name', )
        read_only_fields = ('document_id', 'name', )
