# Guía de Preparación para la Interrogación (Criterio 10 - 6 Puntos)
## Evaluación N°1: Desarrollo Backend con Django & DRF &middot; Docente: Marcelo Alvarado

Esta guía contiene las 4 preguntas fundamentales que se evalúan en la interrogación práctica sobre el proyecto desarrollado:

---

### Pregunta 1: ¿En qué consiste la arquitectura de "Enmascaramiento de Endpoints" en Django y DRF?
**Respuesta sugerida:**
> *"Consiste en separar la entrega visual de la entrega de datos lógicos. 
> 1. Una vista tradicional de Django (`render()`) entrega al navegador el cascarón de la página HTML con estilos Bootstrap en la ruta principal (ej. `/cursos/`).
> 2. Una vez que la página carga, código JavaScript en segundo plano ejecuta peticiones asíncronas (`fetch()`) hacia el endpoint de Django REST Framework (ej. `/api/courses/`).
> 3. JavaScript recibe el JSON puro e inyecta dinámicamente las filas en la tabla del DOM sin necesidad de recargar la página completa."*

---

### Pregunta 2: ¿Cómo se solucionó el "Error 404" en la ruta raíz del servidor?
**Respuesta sugerida:**
> *"Por defecto, en Django/DRF la ruta vacía `http://127.0.0.1:8000/` no tiene nada asignado y genera un error 404 de página no encontrada.
> La solución consistió en:
> 1. Registrar la ruta raíz `path('', views.index_view, name='index')` en `urls.py` vinculada a una vista que renderiza la portada institucional del Sistema Académico.
> 2. Definir un `handler404` personalizado en `academic_project/urls.py` que captura cualquier URL no existente y devuelve una plantilla amigable con código de estado HTTP 404."*

---

### Pregunta 3: ¿Cómo se gestiona la seguridad CSRF en las peticiones destructivas (POST, PUT, DELETE) mediante Fetch?
**Respuesta sugerida:**
> *"Dado que DRF y Django protegen las peticiones de modificación contra ataques CSRF:
> 1. Emitimos el token de seguridad dentro de la plantilla HTML mediante la etiqueta `{% csrf_token %}`.
> 2. En JavaScript, extraemos el token del DOM con `document.querySelector('[name=csrfmiddlewaretoken]').value`.
> 3. Incluimos dicho valor en la cabecera HTTP de la petición Fetch como `'X-CSRFToken': csrfToken`, permitiendo crear, modificar y eliminar registros de manera autorizada."*

---

### Pregunta 4: ¿Cómo se implementó el modelo ER y la relación entre Asignaturas y Docentes?
**Respuesta sugerida:**
> *"Se implementó según el diagrama provisto:
> - En `models.py`, creamos la clase `Teacher` y la clase `Course`. En `Course` definimos una relación de clave foránea `teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_id')` que representa la relación 1 a N ('un docente imparte muchas asignaturas').
> - Para la relación N a M entre Estudiantes y Cursos, creamos la tabla intermedia `StudentCourse` con claves foráneas a `Student` y `Course` y restricción `unique_together`.
> - En `serializers.py`, usamos `CourseSerializer` con un `SerializerMethodField` para devolver el nombre completo del profesor asignado (`teacher_name`), facilitando su renderizado en la tabla."*
