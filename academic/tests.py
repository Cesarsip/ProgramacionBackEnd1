from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Teacher, Course, Student, StudentCourse

class AcademicSystemTests(APITestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(first_name="Marcelo", last_name="Alvarado")
        self.course = Course.objects.create(name="Desarrollo Backend", teacher=self.teacher)
        self.student = Student.objects.create(first_name="César", last_name="Silva")
        self.enrollment = StudentCourse.objects.create(student=self.student, course=self.course)
        self.user = User.objects.create_user(username='api-user', password='safe-password')
        self.client.force_authenticate(user=self.user)

    # --- PRUEBAS DE VISTAS HTML (ENMASCARAMIENTO Y SOLUCIÓN 404) ---
    def test_root_url_solves_404(self):
        """Verifica que la raíz ('/') retorne 200 y no error 404."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/index.html')

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/login.html')

    def test_jwt_login(self):
        response = self.client.post(
            '/api/token/',
            {'username': 'api-user', 'password': 'safe-password'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_courses_view(self):
        """Verifica que la vista de cursos cargue correctamente."""
        response = self.client.get('/cursos/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/courses.html')

    def test_students_view(self):
        """Verifica que la vista de estudiantes cargue correctamente."""
        response = self.client.get('/estudiantes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/students.html')

    # --- PRUEBAS DE ENDPOINTS DRF (API REST) ---
    def test_api_list_teachers(self):
        """Verifica el endpoint GET /api/teachers/."""
        response = self.client.get('/api/teachers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_api_list_courses(self):
        """Verifica el endpoint GET /api/courses/."""
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], "Desarrollo Backend")
        self.assertIn("Prof. Marcelo Alvarado", response.data[0]['teacher_name'])

    def test_api_create_course(self):
        """Verifica el endpoint POST /api/courses/."""
        payload = {"name": "Arquitectura Cloud", "teacher": self.teacher.id}
        response = self.client.post('/api/courses/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.filter(name="Arquitectura Cloud").count(), 1)

    def test_api_list_students(self):
        """Verifica el endpoint GET /api/students/."""
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['first_name'], "César")

    def test_api_student_courses(self):
        """Verifica el endpoint GET /api/student-courses/."""
        response = self.client.get('/api/student-courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['course_name'], "Desarrollo Backend")

    def test_api_requires_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/teachers/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_filters(self):
        self.course.shift = 'vespertina'
        self.course.save(update_fields=['shift'])
        self.student.gender = 'femenino'
        self.student.save(update_fields=['gender'])

        teachers = self.client.get('/api/teachers/?last_name=alvar')
        courses = self.client.get('/api/courses/?shift=VESPERTINA')
        students = self.client.get('/api/students/?gender=FEMENINO')
        enrollments = self.client.get(f'/api/student-courses/?course={self.course.id}')

        self.assertEqual(len(teachers.data), 1)
        self.assertEqual(len(courses.data), 1)
        self.assertEqual(len(students.data), 1)
        self.assertEqual(len(enrollments.data), 1)

    def test_api_documentation(self):
        response = self.client.get('/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
