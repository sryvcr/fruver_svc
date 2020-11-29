from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProvidersListViewSet,
    ProviderByPkViewSet,
)

router = SimpleRouter()
router.register(r'get-list', ProvidersListViewSet)
router.register(r'get-one', ProviderByPkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
