from rest_framework import serializers
from .models import (
  ActivosModel,
  LaboratoriosModel,
  MarcasModel,
  TipoActivosModel
)


class LaboratoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoriosModel
        fields = '__all__'


class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcasModel
        fields = '__all__'


class TipoActivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActivosModel
        fields = '__all__'


class ActivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivosModel
        fields = '__all__'
