from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('miembros/', views.contenido_usuarios, name='contenido_usuarios'),
]
