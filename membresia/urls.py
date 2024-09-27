from django.urls import path
from . import views

urlpatterns = [
    path('', views.membresia, name='membresia'),
]
