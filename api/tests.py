from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import programmer

class BackendViewsAndAPITests(APITestCase):
    def setUp(self):
        self.prog = programmer.objects.create(
            fullname="Alan Turing",
            nickname="aturing",
            language="Assembly / Cryptography",
            age=41,
            is_active=True
        )

    def test_root_url_solves_404(self):
        """Verifica que la ruta raíz ('/') devuelve HTTP 200 y no error 404."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/index.html')

    def test_programmers_view(self):
        """Verifica que la página de gestión de programadores carga correctamente."""
        response = self.client.get('/programadores/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/programmers.html')

    def test_services_view(self):
        """Verifica que la página de servicios carga correctamente."""
        response = self.client.get('/servicios/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/servicios.html')

    def test_contact_view(self):
        """Verifica que la página de contacto carga correctamente."""
        response = self.client.get('/contacto/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/contacto.html')

    def test_drf_api_list_programmers(self):
        """Verifica el endpoint GET /api/programmers/."""
        response = self.client.get('/api/programmers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
        self.assertEqual(response.data[0]['fullname'], "Alan Turing")

    def test_drf_api_create_programmer(self):
        """Verifica el endpoint POST /api/programmers/."""
        payload = {
            "fullname": "Margaret Hamilton",
            "nickname": "apollo_lead",
            "language": "Apollo Assembly",
            "age": 87,
            "is_active": True
        }
        response = self.client.post('/api/programmers/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(programmer.objects.filter(nickname="apollo_lead").count(), 1)

    def test_drf_api_update_programmer(self):
        """Verifica el endpoint PUT /api/programmers/{id}/."""
        payload = {
            "fullname": "Alan Mathison Turing",
            "nickname": "aturing",
            "language": "Theoretical Computing",
            "age": 42,
            "is_active": True
        }
        response = self.client.put(f'/api/programmers/{self.prog.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.prog.refresh_from_db()
        self.assertEqual(self.prog.fullname, "Alan Mathison Turing")

    def test_drf_api_delete_programmer(self):
        """Verifica el endpoint DELETE /api/programmers/{id}/."""
        response = self.client.delete(f'/api/programmers/{self.prog.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(programmer.objects.filter(id=self.prog.id).count(), 0)
