from django.contrib import admin
from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    #path('inicio/', views.inicioTiendaView.as_view(), name='inicio'),
    path('crear/', views.usuario_crear.as_view(), name='crear'),
    path('login/', views.usuario_login.as_view(), name='login'),
]
