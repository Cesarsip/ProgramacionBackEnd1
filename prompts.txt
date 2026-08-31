# Entregable de Inteligencia Artificial (prompts.md)
## Evaluación N°1: Desarrollo Backend con Django & DRF
**Asignatura:** Desarrollo Backend &middot; **Docente:** Marcelo Alvarado &middot; **Carrera:** Informática y Ciberseguridad

Este documento registra la interacción con la herramienta de Inteligencia Artificial (Gemini / Antigravity) de acuerdo con el **Criterio 8** de la pauta de evaluación.

---

### Prompt 1: Generación de Datos Simulados en Formato JSON (Criterio 2)

**Prompt:**
> "Actúa como un asistente de desarrollo backend. Genera una estructura de datos de prueba en formato JSON que represente el modelo entidad-relación del Sistema de Gestión Académica:
> - Entidad `teacher` (id, first_name, last_name)
> - Entidad `course` (id, name, teacher_id como clave foránea a teacher)
> - Entidad `student` (id, first_name, last_name)
> - Entidad `student_course` (student_id, course_id)
> Incluye al docente Marcelo Alvarado y materias representativas del área de informática."

**Respuesta generada por la IA:**
```json
{
  "teachers": [
    { "id": 1, "first_name": "Marcelo", "last_name": "Alvarado" },
    { "id": 2, "first_name": "Alan", "last_name": "Turing" },
    { "id": 3, "first_name": "Ada", "last_name": "Lovelace" },
    { "id": 4, "first_name": "Grace", "last_name": "Hopper" }
  ],
  "courses": [
    { "id": 1, "name": "Desarrollo Backend con Django & DRF", "teacher_id": 1 },
    { "id": 2, "name": "Bases de Datos & Normalización", "teacher_id": 1 },
    { "id": 3, "name": "Teoría de la Computación & Algoritmos", "teacher_id": 2 },
    { "id": 4, "name": "Arquitectura de Software & Microservicios", "teacher_id": 3 }
  ],
  "students": [
    { "id": 1, "first_name": "César", "last_name": "Silva" },
    { "id": 2, "first_name": "Juan", "last_name": "Pérez" },
    { "id": 3, "first_name": "Ana", "last_name": "Ríos" }
  ],
  "student_courses": [
    { "student_id": 1, "course_id": 1 },
    { "student_id": 1, "course_id": 2 },
    { "student_id": 2, "course_id": 1 }
  ]
}
```

---

### Prompt 2: Maquetación Frontend y Enmascaramiento de Endpoints (Criterio 4 y 7)

**Prompt:**
> "Diseña una interfaz web moderna en Bootstrap 5 con tema Dark Mode y acento Rosa (`#ED2C7B`) para el Sistema Académico en Django. 
> La interfaz debe enmascarar los endpoints de DRF:
> 1. `base.html`: Barra de navegación fija con logotipo brillante y enlaces a Cursos, Estudiantes, Docentes e Inscripciones.
> 2. `courses.html`: Vista que muestra la tabla de Cursos y su Profesor asignado. Debe utilizar JavaScript asíncrono (`fetch()`) para consultar `/api/courses/`, inyectar los datos en el DOM y permitir registrar/editar/eliminar asignaturas enviando el token CSRF en la cabecera `X-CSRFToken`.
> 3. `students.html`: Vista de Estudiantes con consumo asíncrono de `/api/students/`.
> 4. Solución al 'error 404' en la ruta raíz (`/`)."

**Respuesta generada por la IA:**
- Creación de la plantilla base `base.html` con inyección de variables CSS personalizadas (`--pink`, `--bg-panel`, etc.) y token CSRF global `{% csrf_token %}`.
- Desarrollo de las vistas `courses.html` y `students.html` con funciones asíncronas `cargarCursos()`, `guardarCurso()`, `actualizarCurso()`, `eliminarCurso()` y modal para selección dinámica de profesores desde `/api/teachers/`.
- Configuración de la ruta raíz en `academic/urls.py` apuntando a `index_view` para eliminar el error 404.

---

### Prompt 3: Construcción de Modelos y Serializadores DRF (Criterio 1 y 6)

**Prompt:**
> "Escribe el código en Python para los modelos de Django (`models.py`) y serializadores de Django REST Framework (`serializers.py`) respetando el modelo ER provisto. En el serializador de Course, incluye un campo calculado `teacher_name` para que el frontend reciba el nombre del profesor sin necesidad de hacer múltiples consultas."

**Respuesta generada por la IA:**
- Modelos `Teacher`, `Course` (con `ForeignKey` a `Teacher`), `Student` y `StudentCourse` (con `unique_together`).
- Serializadores `TeacherSerializer`, `CourseSerializer` (con `SerializerMethodField` para `teacher_name`), `StudentSerializer` y `StudentCourseSerializer`.
