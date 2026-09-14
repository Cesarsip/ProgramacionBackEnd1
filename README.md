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

## Guía de instalación y consumo de la API

### Instalación

Se recomienda crear y activar un entorno virtual antes de instalar las
dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

`requirements.txt` incorpora `djangorestframework`, `djangorestframework-simplejwt`,
`coreapi`, `django-filter` y `drf-yasg`. CoreAPI se conserva como librería
externa para `/docs/`; Swagger/OpenAPI se expone como documentación principal
en `/swagger/` y `/swagger.json`.

### Qué hace cada bloque y qué ocurre si se elimina

En [settings.py](./academic_project/settings.py), el bloque `INSTALLED_APPS`
registra DRF y `django_filters`; si se elimina una de esas entradas, Django no
podrá cargar esa integración. El bloque `REST_FRAMEWORK` selecciona JWT,
`IsAuthenticated`, filtros y `AutoSchema`; si se elimina, la API puede volver a
usar autenticación por sesión, dejar endpoints sin protección o no generar el
esquema CoreAPI.

En [models.py](./academic/models.py), `*_CHOICES` restringe los datos válidos:
sexo `M/F` (Masculino/Femenino), jornada `D/V` (Despertino/Vespertino) y tipo
de profesor `CH/CD` (Jornada por hora/Jornada definida). Si se elimina
`choices`, Django y el serializer aceptarían valores arbitrarios.

En [serializers.py](./academic/serializers.py), `ModelSerializer` valida el
JSON y lo convierte a modelos; si se elimina un campo, ese dato no aparecerá
en respuestas ni podrá enviarse desde la API.

En [views.py](./academic/views.py), cada `ModelViewSet` habilita el CRUD y
declara su permiso. Si se elimina un ViewSet o su registro en el router, esa
entidad deja de tener sus rutas CRUD. `IsAuthenticated` protege profesores,
estudiantes y cursos. `ReadOnlyOrAuthenticated` permite consultar asignaturas
sin login, pero exige JWT para crear, modificar o eliminar.

En [filters.py](./academic/filters.py), cada `FilterSet` traduce parámetros
como `last_name`, `course`, `gender` y `shift` a consultas seguras del ORM.
Si se elimina el filtro o `DjangoFilterBackend`, los parámetros URL se
ignoran.

En [academic_project/urls.py](./academic_project/urls.py), las rutas JWT son
las que emiten y renuevan tokens; Swagger usa `drf-yasg` para construir el
contrato OpenAPI. Si se elimina una ruta, el endpoint correspondiente dejará
de existir, aunque el código de la vista permanezca.

### Seguridad y documentación

Los cuatro ViewSet (`teachers`, `courses`, `students` y `student-courses`)
declaran `IsAuthenticated` explícitamente. La autenticación de la API usa
Bearer JWT:

- `POST http://127.0.0.1:8000/api/token/`
- `POST http://127.0.0.1:8000/api/token/refresh/`
- `GET http://127.0.0.1:8000/docs/` (documentación interactiva CoreAPI)
- `GET http://127.0.0.1:8000/swagger/` (interfaz Swagger UI)
- `GET http://127.0.0.1:8000/swagger.json` (especificación OpenAPI)

Crear un usuario con `createsuperuser` o desde `/admin/`. En Postman, guardar
el valor `access` de la respuesta del primer endpoint y enviar en cada
operación protegida:

```text
Authorization: Bearer <access>
```

Solicitud para obtener tokens:

```http
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "tu-clave"
}
```

Renovación:

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "<refresh>"
}
```

### CRUD disponible

Profesores, estudiantes y cursos requieren JWT y exponen `GET` de colección y
detalle, `POST`, `PUT`, `PATCH` y `DELETE` mediante `ModelViewSet`.
Asignaciones (`student-courses`) permiten `GET` público de solo lectura; sus
operaciones `POST`, `PUT`, `PATCH` y `DELETE` requieren JWT:

```text
/api/teachers/
/api/courses/
/api/students/
/api/student-courses/
```

Los identificadores de relaciones se envían como enteros. Por ejemplo, para
crear un curso:

```json
{
  "name": "Desarrollo Backend",
  "shift": "V",
  "teacher": 1
}
```

### Filtros probados en Postman

Todos los ejemplos requieren el encabezado `Authorization`:

```text
GET /api/teachers/?last_name=alvarado
GET /api/courses/?course=backend
GET /api/courses/?shift=V
GET /api/students/?last_name=silva
GET /api/students/?gender=F
GET /api/student-courses/?course=1
```

`last_name` realiza una búsqueda parcial sin distinguir mayúsculas; `course`
busca parcialmente por el nombre del curso en `/api/courses/` y por el
identificador relacionado en `/api/student-courses/`; `gender` y `shift`
realizan comparación exacta sin distinguir mayúsculas.
