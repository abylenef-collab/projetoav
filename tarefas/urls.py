from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
]