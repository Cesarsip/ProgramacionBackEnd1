from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer
from .filters import CourseFilter, StudentCourseFilter, StudentFilter, TeacherFilter

# =====================================================================
# VISTAS DE PLANTILLAS HTML (ENMASCARAMIENTO DE ENDPOINTS)
# Cumple Criterio 3 y 7: Renderizado de interfaces web tradicionales
# =====================================================================

def index_view(request):
    """
    Vista de Inicio / Portada del Sistema Académico.
    Soluciona el 'error 404' al acceder a la ruta raíz ('/').
    """
    return render(request, 'academic/index.html')


def login_view(request):
    """Renderiza el formulario de acceso de la interfaz web."""
    return render(request, 'academic/login.html')


def courses_view(request):
    """
    Vista de Cursos: 'Máscara' visual que renderiza el cascarón HTML.
    JavaScript fetch() consume /api/courses/ en segundo plano.
    """
    return render(request, 'academic/courses.html')


def students_view(request):
    """
    Vista de Estudiantes: 'Máscara' visual que renderiza el cascarón HTML.
    JavaScript fetch() consume /api/students/ en segundo plano.
    """
    return render(request, 'academic/students.html')


def teachers_view(request):
    """
    Vista de Docentes: 'Máscara' visual que renderiza el cascarón HTML.
    JavaScript fetch() consume /api/teachers/ en segundo plano.
    """
    return render(request, 'academic/teachers.html')


def enrollments_view(request):
    """
    Vista de Inscripciones (StudentCourse): Relación N a M.
    JavaScript fetch() consume /api/student-courses/ en segundo plano.
    """
    return render(request, 'academic/enrollments.html')


def custom_404_view(request, exception=None):
    """
    Manejador personalizado de error 404 para redirigir al usuario
    de forma segura ante rutas no encontradas.
    """
    return render(request, '404.html', status=404)


# =====================================================================
# VIEWSETS DE DJANGO REST FRAMEWORK (API REST)
# Cumple Criterio 5 y 6: Endpoints consumidos de forma asíncrona
# =====================================================================

class TeacherViewSet(viewsets.ModelViewSet):
    """Endpoint REST CRUD para la entidad Teacher (/api/teachers/)."""
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter


class CourseViewSet(viewsets.ModelViewSet):
    """Endpoint REST CRUD para la entidad Course (/api/courses/)."""
    queryset = Course.objects.select_related('teacher').all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class StudentViewSet(viewsets.ModelViewSet):
    """Endpoint REST CRUD para la entidad Student (/api/students/)."""
    queryset = Student.objects.prefetch_related('student_courses__course').all().order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter


class StudentCourseViewSet(viewsets.ModelViewSet):
    """Endpoint REST CRUD para la entidad StudentCourse (/api/student-courses/)."""
    queryset = StudentCourse.objects.select_related('student', 'course').all().order_by('id')
    serializer_class = StudentCourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentCourseFilter
