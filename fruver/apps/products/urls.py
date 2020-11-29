from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProductsListViewSet,
    ProductByPkViewSet
)

router = SimpleRouter()
router.register(r'get-list', ProductsListViewSet)
router.register(r'get-one', ProductByPkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
