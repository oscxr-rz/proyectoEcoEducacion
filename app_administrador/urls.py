from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrador, name='administrador'),
    path('logout/', views.adminLogout, name='adminLogout'),
    path('agregar nuevo administrador/', views.register, name='register'),
    path('cambiar contraseña/', views.newPassword, name='newPassword'),
    path('estadisticas de juego/', views.estadisticas, name='estadisticas'),
    path('tablas de juego/', views.tablas, name='tablas'),
]
