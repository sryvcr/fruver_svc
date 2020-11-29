from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProductsListViewSet,
    ProductByPkViewSet,
    ProductCreateOneView,
)

router = SimpleRouter()
router.register(r'get-list', ProductsListViewSet)
router.register(r'get-one', ProductByPkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-one', view=ProductCreateOneView.as_view(), name='products_create_one')
]
