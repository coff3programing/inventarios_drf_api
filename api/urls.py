from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
  LaboratoriosViewSet,
  MarcasViewSet,
  TipoActivosViewSet,
  ActivosViewSet
)

router = DefaultRouter()
router.register(r'laboratorios', LaboratoriosViewSet)
router.register(r'marcas', MarcasViewSet)
router.register(r'tipoactivos', TipoActivosViewSet)
router.register(r'activos', ActivosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
