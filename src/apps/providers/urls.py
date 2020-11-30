from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf.urls import include
from .views import (
    ProvidersListViewSet,
    ProviderByPkViewSet,
    ProviderCreateOneView,
    ProviderUpdateOneView,
    ProviderDeleteOneView,
)

router = SimpleRouter()
router.register(r'get-list', ProvidersListViewSet)
router.register(r'get-one', ProviderByPkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-one', view=ProviderCreateOneView.as_view(), name='provider_create_one'),
    path('update-one/<str:document_id>', view=ProviderUpdateOneView.as_view(), name='provider_update_one'),
    path('delete-one/<str:document_id>', view=ProviderDeleteOneView.as_view(), name='provider_delete_one'),
]
