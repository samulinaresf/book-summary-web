from django.urls import path
from . import views
from django.db.models import Q

urlpatterns = [
    path('', views.mostrar_resumenes, name='resumenes'),
    #path('<slug:slug_categoria>', views.mostrar_resumenes, name="por-categoria"),
    #path('<slug:slug_autor>/', views.libros_por_autor, name='por-autor'),
    path('search/', views.busqueda_producto, name="busqueda")
]
