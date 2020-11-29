from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    viewsets,
    status
)
from .models import (
    Providers,
)
from .serializers import (
    ProvidersSerializer
)


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


class ProvidersListViewSet(ReadOnlyViewSet):

    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

    def get_queryset(self):
        queryset = Providers.objects.all()
        name = self.request.query_params.get('name', None)
        document_id = self.request.query_params.get('document_id', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if document_id:
            queryset = queryset.filter(document_id__icontains=document_id)
        return queryset


class ProviderByPkViewSet(ReadOnlyViewSet):

    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

    def retrieve(self, request, *args, **kwargs):
        document_id = self.kwargs['pk']
        try:
            queryset = Providers.objects.get(pk=document_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProvidersSerializer(queryset)
        response = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(response)
