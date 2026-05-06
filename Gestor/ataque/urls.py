# ataque/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('configuracion-sensible/', views.ruta_critica_view, name='sensible'),
]