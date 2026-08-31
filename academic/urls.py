from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academic import views

# Enrutador REST para los endpoints de la API
router = DefaultRouter()
router.register(r'teachers', views.TeacherViewSet, basename='teacher')
router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'student-courses', views.StudentCourseViewSet, basename='student-course')

urlpatterns = [
    # Vistas de Plantillas HTML (Enmascaramiento)
    path('', views.index_view, name='index'),
    path('cursos/', views.courses_view, name='courses'),
    path('estudiantes/', views.students_view, name='students'),
    path('docentes/', views.teachers_view, name='teachers'),
    path('inscripciones/', views.enrollments_view, name='enrollments'),

    # Endpoints REST API consumidos por JavaScript fetch()
    path('api/', include(router.urls)),
]
