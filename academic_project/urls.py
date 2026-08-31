from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academic.urls')),
]

# Manejador personalizado de error 404
handler404 = 'academic.views.custom_404_view'
