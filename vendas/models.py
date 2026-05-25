from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Medicamento(models.Model):
    nome = models.CharField(max_length=255)
    principio_ativo = models.CharField(max_length=255, blank=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    data_validade = models.DateField()
    tarja_preta = models.BooleanField(default=False)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome 

class Suplemento(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, blank=True) 
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    data_validade = models.DateField()
    e_importado = models.BooleanField(default=False) 
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome