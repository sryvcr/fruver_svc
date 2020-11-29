from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializer
from fruver_utils.readonly_viewset import ReadOnlyViewSet


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
