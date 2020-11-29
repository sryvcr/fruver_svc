from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import (
    viewsets,
    status,
)
from fruver_utils.readonly_viewset import ReadOnlyViewSet
from fruver_utils.make_response import make_response
from .models import Products
from .serializers import ProductsSerializer


class ProductsListViewSet(ReadOnlyViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        name = self.request.query_params.get('name', None)
        providers_id = self.request.query_params.get('providers_id', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if providers_id:
            queryset = queryset.filter(providers__document_id__icontains=providers_id)
        return queryset


class ProductByPkViewSet(ReadOnlyViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def retrieve(self, request, *args, **kwargs):
        _id = self.kwargs['pk']
        try:
            queryset = Products.objects.get(pk=_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductsSerializer(queryset)
        response = make_response(status.HTTP_200_OK, serializer.data)
        return Response(response)
