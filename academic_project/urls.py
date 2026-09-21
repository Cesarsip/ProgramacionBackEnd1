from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from academic import views

# Define el documento OpenAPI que consumirá Swagger UI. Si se elimina, las
# rutas /swagger/ y /swagger.json no podrán construir la documentación.
schema_view = get_schema_view(
    openapi.Info(
        title='Academic API',
        default_version='v1',
        description='API académica protegida con JWT.',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # JWT: token de acceso para consumir la API y refresh para renovarlo.
    # Sin estas rutas, el login no podría autenticarse contra DRF.
    path('admin/', admin.site.urls),
    path('', include('academic.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # CoreAPI se mantiene porque forma parte del requisito original.
    path('docs/', include_docs_urls(title='Academic API', public=False)),
    # Swagger UI permite explorar/probar la API; swagger.json entrega el
    # contrato OpenAPI para herramientas externas.
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    re_path(r'^(?P<path>.*)$', views.fallback_view, name='fallback'),
]

# Manejador personalizado de error 404
handler404 = 'academic.views.custom_404_view'
