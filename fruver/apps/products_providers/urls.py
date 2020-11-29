from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProvidersListViewSet
)

router = SimpleRouter()
router.register(r'get-list', ProvidersListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
