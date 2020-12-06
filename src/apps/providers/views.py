import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    viewsets,
    status,
)
from gs_utils.readonly_viewset import ReadOnlyViewSet
from gs_utils.make_response import make_response
from .models import Providers
from .serializers import ProvidersSerializer


class ProvidersListViewSet(viewsets.ReadOnlyModelViewSet):

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
            response = make_response(status.HTTP_404_NOT_FOUND, {})
            return Response(status=status.HTTP_404_NOT_FOUND, data=response)
        serializer = ProvidersSerializer(queryset)
        response = make_response(status.HTTP_200_OK, serializer.data)
        return Response(status=status.HTTP_200_OK, data=response)


class ProviderCreateOneView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            body = json.loads(request.body)
            provider = Providers(
                document_id=body['document_id'],
                name=body['name'],
            )
            provider.save()
            serializer = ProvidersSerializer(provider)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class ProviderUpdateOneView(APIView):

    permission_classes = (IsAuthenticated, )

    def put(self, request, document_id: str):
        try:
            try:
                provider = Providers.objects.get(pk=document_id)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
            body = json.loads(request.body)
            if body['name']:
                provider.name = body['name']
            provider.save()
            serializer = ProvidersSerializer(provider)
            response = make_response(status.HTTP_200_OK, serializer.data)
            return Response(status=status.HTTP_200_OK, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class ProviderDeleteOneView(APIView):

    permission_classes = (IsAuthenticated, )

    def delete(self, request, document_id: str):
        try:
            try:
                provider = Providers.objects.get(pk=document_id)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
            provider.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
