# Sistema de Gestión Académica &middot; Evaluación N°1 Backend (Django & DRF)
## Docente: Marcelo Alvarado &middot; Carrera: Informática y Ciberseguridad &middot; INACAP

Este repositorio contiene la solución completa a la **Evaluación N°1: Desarrollo Backend con Django & DRF** (Ponderación 15%), estructurada según el modelo entidad-relación entregado y aplicando la arquitectura de **enmascaramiento de endpoints** mediante plantillas HTML y consumo asíncrono con JavaScript Fetch.

---

## 🏛️ Estructura del Proyecto

```
ProgramacionBackEnd_Eva1/
│
├── manage.py
├── prompts.md                   # Entregable de IA (Criterio 8)
├── INTERROGACION.md             # Guía de preguntas y respuestas para la evaluación oral
├── README.md                    # Documentación del proyecto
│
├── data/
│   └── academic_mock.json       # Datos simulados en formato JSON (Criterio 2)
│
├── academic_project/            # Configuración del proyecto Django (Criterio 1)
│   ├── settings.py              # Configuración de apps, DRF y templates
│   ├── urls.py                  # URLs raíz y manejador handler404
│   ├── asgi.py
│   └── wsgi.py
│
├── academic/                    # Aplicación de gestión académica (Criterio 1)
│   ├── models.py                # Modelos ER: Teacher, Course, Student, StudentCourse
│   ├── serializers.py           # Serializadores DRF (Criterio 6)
│   ├── views.py                 # Dualidad: Vistas HTML render() y ViewSets DRF
│   ├── urls.py                  # Rutas expuestas y DefaultRouter (/api/...)
│   ├── admin.py                 # Registro en panel de administración Django
│   ├── tests.py                 # Suite de pruebas unitarias automatizadas
│   └── apps.py
│
└── templates/academic/          # Plantillas HTML con tema Dark Mode + Acento Rosa
    ├── base.html                # Menú de navegación Bootstrap y CSRF Token global
    ├── index.html               # Solución al error 404 en la raíz ("/")
    ├── courses.html             # Listado de Cursos y su Profesor asignado (Fetch API)
    ├── students.html            # Listado de Estudiantes (Fetch API)
    ├── teachers.html            # Listado de Docentes (Fetch API)
    ├── enrollments.html         # Inscripciones de alumnos en cursos (Relación N:M)
    └── 404.html                 # Manejador personalizado de error 404
```

---

## 🚀 Instrucciones de Ejecución

### 1. Iniciar el Servidor de Desarrollo
```powershell
py manage.py runserver
```

---

## 🔑 Rutas y Credenciales de Acceso

- **Portada / Inicio (Solución Error 404):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Cursos y Profesores Asignados:** [http://127.0.0.1:8000/cursos/](http://127.0.0.1:8000/cursos/)
- **Listado de Estudiantes:** [http://127.0.0.1:8000/estudiantes/](http://127.0.0.1:8000/estudiantes/)
- **Listado de Docentes:** [http://127.0.0.1:8000/docentes/](http://127.0.0.1:8000/docentes/)
- **Inscripciones (N:M):** [http://127.0.0.1:8000/inscripciones/](http://127.0.0.1:8000/inscripciones/)
- **Endpoints API REST (DRF):**
  - `/api/teachers/`
  - `/api/courses/`
  - `/api/students/`
  - `/api/student-courses/`
- **Panel Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Usuario:** `profe`
  - **Contraseña:** `123456`

---

## 🧪 Ejecución de Pruebas Automatizadas

```powershell
py manage.py test
```
