from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProductsListViewSet,
)

router = SimpleRouter()
router.register(r'get-list', ProductsListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
