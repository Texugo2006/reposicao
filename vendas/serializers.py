from rest_framework import serializers
from .models import Medicamento, Suplemento, Fornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'telefone']

class MedicamentoSerializer(serializers.ModelSerializer):
    fornecedor_nome = serializers.CharField(source='fornecedor.nome', read_only=True)

    class Meta:
        model = Medicamento
        fields = [
            'id', 
            'nome', 
            'principio_ativo', 
            'preco_venda', 
            'quantidade_estoque', 
            'data_validade', 
            'tarja_preta', 
            'fornecedor', 
            'fornecedor_nome'
        ]

class SuplementoSerializer(serializers.ModelSerializer):
    fornecedor_nome = serializers.CharField(source='fornecedor.nome', read_only=True)

    class Meta:
        model = Suplemento
        fields = [
            'id', 
            'nome', 
            'marca', 
            'preco_venda', 
            'quantidade_estoque', 
            'data_validade', 
            'e_importado', 
            'fornecedor', 
            'fornecedor_nome'
        ]