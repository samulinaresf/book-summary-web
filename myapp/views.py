from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contenido_usuarios(request):
    return render(request, 'contenido_usuarios.html')

