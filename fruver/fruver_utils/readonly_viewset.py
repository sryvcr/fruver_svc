from rest_framework import (
    viewsets,
    status,
)
from rest_framework.response import Response


class ReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, *kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        response = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(response)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(response)
