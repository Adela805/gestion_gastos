from django.urls import path 
from . import views
urlpatterns = [
    path('', views.lista_gastos, name='lista'),
    path('crear/', views.crear_gasto, name='crear'),
    path('editar/<int:id>/', views.editar_gasto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_gasto, name='eliminar'),
]

