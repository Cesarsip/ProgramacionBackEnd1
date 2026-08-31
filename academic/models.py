from django.db import models

# =====================================================================
# MODELOS DE DATOS DEL SISTEMA ACADÉMICO (MODELO ENTIDAD-RELACIÓN)
# Cumple Criterio 1: Definición de entidades Teacher, Course, Student, StudentCourse
# =====================================================================

class Teacher(models.Model):
    """
    Entidad Docente (teacher)
    Representa a los profesores que imparten las asignaturas.
    """
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return f"Prof. {self.first_name} {self.last_name}"


class Course(models.Model):
    """
    Entidad Asignatura (course)
    Representa los cursos impartidos por un docente (Relación 1 a N).
    """
    name = models.CharField(max_length=150, verbose_name="Nombre de Asignatura")
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE, 
        related_name='courses',
        db_column='teacher_id',
        verbose_name="Docente Asignado"
    )

    class Meta:
        db_table = 'course'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        return f"{self.name} ({self.teacher.first_name} {self.teacher.last_name})"


class Student(models.Model):
    """
    Entidad Estudiante (student)
    Representa a los alumnos matriculados en la institución.
    """
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")

    class Meta:
        db_table = 'student'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    """
    Entidad Intermedia Inscripciones (student_course)
    Relación N a M entre Estudiantes y Asignaturas.
    """
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='student_courses',
        db_column='student_id',
        verbose_name="Estudiante"
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='student_courses',
        db_column='course_id',
        verbose_name="Asignatura"
    )

    class Meta:
        db_table = 'student_course'
        verbose_name = 'Inscripción de Curso'
        verbose_name_plural = 'Inscripciones de Cursos'
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} inscrito en {self.course.name}"
