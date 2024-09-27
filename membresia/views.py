from django.shortcuts import render
from .models import Membresia
from django.contrib.auth.decorators import login_required

def membresia(request):
    """Página de membresía principal"""
    return render(request, 'membresia.html')

@login_required
def suscripcion_mensual(request):
    """Manejo de la suscripción mensual"""
    user = request.user  # Obtenemos el usuario logueado
    membresia, created = Membresia.objects.get_or_create(username=user)

    # Llamamos al método para aplicar la suscripción mensual
    membresia.suscripcion_mensual()

    # Creamos el contexto con los datos actualizados
    context = {
        'date_joined': membresia.date_joined,
        'date_expired': membresia.date_expired,
        'subtotal': membresia.subtotal,
        'tax': membresia.tax,
        'total': membresia.total
    }

    return render(request, 'membresia.html', context)

@login_required
def suscripcion_anual(request):
    """Manejo de la suscripción anual"""
    user = request.user  # Obtenemos el usuario logueado
    membresia, created = Membresia.objects.get_or_create(username=user)
    

    # Llamamos al método para aplicar la suscripción anual
    membresia.suscripcion_anual()
    
    # Creamos el contexto con los datos actualizados
    context = {
            'date_joined': membresia.date_joined,
            'date_expired': membresia.date_expired,
            'subtotal': membresia.subtotal,
            'tax': membresia.tax,
            'total': membresia.total
        }

    return render(request, 'membresia.html', context)
