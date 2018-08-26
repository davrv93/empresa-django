
from ..models.departamento import Departamento
from rest_framework import serializers, viewsets

# Serializers define the API representation.


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre')

# ViewSets define the view behavior.


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = ()
