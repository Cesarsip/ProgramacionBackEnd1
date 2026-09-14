import django_filters

from .models import Course, Student, StudentCourse, Teacher

# Cada FilterSet convierte parámetros de URL en consultas ORM parametrizadas.
# Si se elimina un FilterSet o su registro en el ViewSet, ese filtro deja de
# funcionar aunque el endpoint continúe respondiendo.

class TeacherFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        field_name='last_name',
        lookup_expr='icontains',
    )
    teacher_type = django_filters.CharFilter(field_name='teacher_type', lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = ('last_name', 'teacher_type')


class CourseFilter(django_filters.FilterSet):
    course = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )
    shift = django_filters.CharFilter(field_name='shift', lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ('course', 'shift')


class StudentFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        field_name='last_name',
        lookup_expr='icontains',
    )
    gender = django_filters.CharFilter(field_name='gender', lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ('last_name', 'gender')


class StudentCourseFilter(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name='course_id')

    class Meta:
        model = StudentCourse
        fields = ('course',)
