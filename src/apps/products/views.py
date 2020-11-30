import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    viewsets,
    status,
)
from fruver_utils.readonly_viewset import ReadOnlyViewSet
from fruver_utils.make_response import make_response
from .models import Products
from ..providers.models import Providers
from .serializers import ProductsSerializer


class ProductsListViewSet(viewsets.ReadOnlyModelViewSet):

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
            response = make_response(status.HTTP_404_NOT_FOUND, {})
            return Response(status=status.HTTP_404_NOT_FOUND, data=response)
        serializer = ProductsSerializer(queryset)
        response = make_response(status.HTTP_200_OK, serializer.data)
        return Response(status=status.HTTP_200_OK, data=response)


class ProductCreateOneView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            body = json.loads(request.body)
            product = Products(
                name=body['name'],
                price=body['price'],
                providers=Providers(document_id=body['providers_id']),
            )
            product.save()
            serializer = ProductsSerializer(product)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
