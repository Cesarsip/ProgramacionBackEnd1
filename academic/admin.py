from django.contrib import admin
from .models import Teacher, Course, Student, StudentCourse

# =====================================================================
# REGISTRO EN DJANGO ADMIN
# Permite la gestión directa desde el panel de administración
# =====================================================================

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('id',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')
    ordering = ('id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('id',)


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
    list_filter = ('course', 'student')
    ordering = ('id',)
