from django.shortcuts import render
from rest_framework import viewsets
from .models import programmer
from .serializer import ProgrammerSerializer

# 1. Vistas de Plantilla (Sustituyen la interfaz nativa y dan estructura web)
def index_view(request):
    """Vista de Inicio / Home: Soluciona el error 404 de la raíz."""
    return render(request, 'api/index.html')

def inicio_view(request):
    """Alias para la vista de inicio."""
    return render(request, 'api/inicio.html')

def programmers_view(request):
    """Vista de Gestión de Programadores: Máscara visual sobre el endpoint DRF."""
    return render(request, 'api/programmers.html')

def services_view(request):
    """Vista de Servicios corporativos."""
    return render(request, 'api/servicios.html')

def contact_view(request):
    """Vista de Contacto."""
    return render(request, 'api/contacto.html')

def login_view(request):
    """Vista de Inicio de Sesión."""
    return render(request, 'api/login.html')

def custom_404_view(request, exception=None):
    """Manejador personalizado de páginas no encontradas (404)."""
    return render(request, '404.html', status=404)

# 2. Vista de API REST (Endpoint consumido en segundo plano)
class ProgrammerViewSet(viewsets.ModelViewSet):
    """ModelViewSet para operaciones CRUD de la API REST."""
    queryset = programmer.objects.all().order_by('id')
    serializer_class = ProgrammerSerializer
