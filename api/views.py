from rest_framework import viewsets, filters
from .models import (
    LaboratoriosModel,
    MarcasModel,
    TipoActivosModel,
    ActivosModel
)
from .serializers import (
    LaboratoriosSerializer,
    MarcasSerializer,
    TipoActivosSerializer,
    ActivosSerializer
)


class LaboratoriosViewSet(viewsets.ModelViewSet):
    queryset = LaboratoriosModel.objects.all()
    serializer_class = LaboratoriosSerializer


class MarcasViewSet(viewsets.ModelViewSet):
    queryset = MarcasModel.objects.all()
    serializer_class = MarcasSerializer


class TipoActivosViewSet(viewsets.ModelViewSet):
    queryset = TipoActivosModel.objects.all()
    serializer_class = TipoActivosSerializer


class ActivosViewSet(viewsets.ModelViewSet):
    queryset = ActivosModel.objects.all()
    serializer_class = ActivosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo_activo']
