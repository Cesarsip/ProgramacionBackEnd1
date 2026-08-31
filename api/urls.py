from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet, basename='programmer')

urlpatterns = [
    # Vistas de Plantilla HTML
    path('', views.index_view, name='index'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('programadores/', views.programmers_view, name='programmers'),
    path('servicios/', views.services_view, name='services'),
    path('contacto/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    
    # Endpoints REST API consumidos en segundo plano
    path('api/', include(router.urls)),
]
