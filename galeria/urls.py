from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar/<int:foto_id>', editar, name='editar'),
    path('deletar/<int:foto_id>', deletar, name='deletar'),
]
