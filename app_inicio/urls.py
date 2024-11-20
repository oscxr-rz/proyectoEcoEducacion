from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('deforestacion en ocotlán de morelos/', views.deforestacion, name='deforestacion'),
    path('contaminacion del agua en ocotlán de morelos/', views.contaminacionAgua, name='contaminacionAgua'),
    path('contaminacion del aire en ocotlán de morelos/', views.contaminacionAire, name='contaminacionAire'),
    path('explotación de los recursos naturales en ocotlán de morelos/', views.recursosNaturales, name='recursosNaturales'),
    path('registro de usuarios/', views.usuario, name='usuario'),
    path('acerca de/', views.about, name='about'),
]
