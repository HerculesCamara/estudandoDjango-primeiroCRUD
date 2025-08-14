from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.tarefas_adicionar, name='tarefas_adicionar'),
    path('remover/<int:id>/', views.tarefas_remover, name='tarefas_remover'),
    path('editar/<int:id>/', views.tarefas_editar, name='tarefas_editar'),
]