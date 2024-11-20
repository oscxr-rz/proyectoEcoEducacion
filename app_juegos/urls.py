from django.urls import path
from . import views

urlpatterns = [
    path('menu de juegos/', views.menu, name='menu'),
    path('juego de quiz/', views.quiz, name='quiz'),
    path('tabla de puntuaciones/', views.puntuacion, name='puntuacion'),
    path('admin form/', views.adminLogin,  name='adminLogin'),
]
