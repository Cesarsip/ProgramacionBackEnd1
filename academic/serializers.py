from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

# =====================================================================
# SERIALIZADORES DJANGO REST FRAMEWORK (serializers.py)
# Cumple Criterio 6: Mapeo de entidades a formato JSON y viceversa
# =====================================================================

class TeacherSerializer(serializers.ModelSerializer):
    """Serializador para la entidad Teacher (Docentes)."""
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'teacher_type']


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializador para la entidad Course (Asignaturas).
    Incluye el nombre del profesor asignado para facilitar el consumo del frontend.
    """
    teacher_name = serializers.SerializerMethodField(read_only=True)
    # Este campo es calculado y solo lectura; facilita mostrar el profesor sin
    # hacer otra petición. Si se elimina, la API devolverá solo teacher (ID).

    class Meta:
        model = Course
        fields = [
            'id', 'code', 'name', 'description', 'credits', 'semester',
            'shift', 'teacher', 'teacher_name',
        ]

    def get_teacher_name(self, obj):
        if obj.teacher:
            return f"Prof. {obj.teacher.first_name} {obj.teacher.last_name}"
        return "Sin profesor asignado"


class StudentSerializer(serializers.ModelSerializer):
    """Serializador para la entidad Student (Estudiantes)."""
    enrolled_courses = serializers.SerializerMethodField(read_only=True)
    # Expone nombres de cursos inscritos sin permitir que el cliente modifique
    # la relación desde este serializer.

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'enrolled_courses']

    def get_enrolled_courses(self, obj):
        # Obtener los nombres de los cursos en los que está inscrito el estudiante
        return [sc.course.name for sc in obj.student_courses.all()]


class StudentCourseSerializer(serializers.ModelSerializer):
    """Serializador para la entidad intermedia StudentCourse (Inscripciones)."""
    student_name = serializers.SerializerMethodField(read_only=True)
    course_name = serializers.SerializerMethodField(read_only=True)
    # Los nombres son informativos; student y course siguen siendo los IDs
    # usados para crear o modificar la asignación.

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course', 'student_name', 'course_name']

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    def get_course_name(self, obj):
        return obj.course.name
