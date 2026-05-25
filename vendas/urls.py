from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicamentoViewSet, SuplementoViewSet, FornecedorViewSet

router = DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet, basename='fornecedor')
router.register(r'medicamentos', MedicamentoViewSet, basename='medicamento')
router.register(r'suplementos', SuplementoViewSet, basename='suplemento')

urlpatterns = [
    path('', include(router.urls)),
]