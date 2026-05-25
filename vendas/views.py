from rest_framework import viewsets
from .models import Medicamento, Suplemento, Fornecedor
from .serializers import MedicamentoSerializer, SuplementoSerializer, FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class SuplementoViewSet(viewsets.ModelViewSet):
    queryset = Suplemento.objects.all()
    serializer_class = SuplementoSerializer