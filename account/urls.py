from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

router = DefaultRouter()

router.register('persons', PersonViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]