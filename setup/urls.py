from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),  # Redireciona as rotas para o app tarefas
]