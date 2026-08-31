# Evaluación 1: Programación BackEnd (INACAP) Ejercicio 
## Solución al "Error 404" & Sustitución / Enmascaramiento de Endpoints DRF mediante Plantillas HTML

Este proyecto corresponde al desarrollo integral de la **Evaluación 1 (Tareas 1 y 2)**, implementado con **Django 6.1** y **Django REST Framework (DRF) 3.18**.

---

## 🏛️ Contexto del Proyecto

- **Empresa / Proyecto:** **TechNova Solutions** (Plataforma y consultora de ingeniería de software backend).
- **Profesor:** Marcelo Alvarado.
- **Asignatura:** Programación BackEnd / Informática y Ciberseguridad.

---

## 🚀 Características Principales

1. **Solución Definitiva al "Error 404":**
   - Se erradica la pantalla por defecto 404 en la raíz del servidor (`http://127.0.0.1:8000/`) enrutándola a una vista de inicio profesional (`index.html`).
   - Se incluye un manejador `handler404` con una plantilla personalizada (`404.html`) que orienta al usuario en caso de rutas inexistentes.

2. **Esquema Web Completo (Vistas HTML):**
   - **Inicio (`/`):** Portal corporativo con métricas y resumen de arquitectura.
   - **Gestión de Programadores (`/programadores/`):** Interfaz interactiva para administrar desarrolladores (CRUD en tiempo real).
   - **Servicios (`/servicios/`):** Catálogo de soluciones backend con mención a la normalización de bases de datos (1NF, 2NF, 3NF).
   - **Contacto (`/contacto/`):** Formulario de contacto empresarial.

3. **Arquitectura de Sustitución y Enmascaramiento:**
   - **Backend Dual:** Separación entre la entrega de plantillas tradicionales (`render()`) y el consumo puro de datos REST (`ModelViewSet`).
   - **Consumo Asíncrono:** La plantilla HTML (`programmers.html`) consume `/api/programmers/` en segundo plano utilizando JavaScript moderno (`fetch()`).
   - **Seguridad CSRF:** Cada petición destructiva (`POST`, `PUT`, `DELETE`) inyecta el token de seguridad `X-CSRFToken` capturado del DOM.
   - **Inspector JSON en Vivo:** Panel interactivo para visualizar el payload JSON que retorna DRF en tiempo real.

---

## ⚙️ Instrucciones de Ejecución

### 1. Activar entorno virtual (si aplica)
```powershell
.\env\Scripts\activate
```

### 2. Ejecutar Migraciones (ya aplicadas por defecto en SQLite)
```powershell
py manage.py makemigrations
py manage.py migrate
```

### 3. Iniciar el Servidor de Desarrollo
```powershell
py manage.py runserver
```

---

## 🔑 Credenciales de Acceso

- **URL del Sitio Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Gestión de Programadores:** [http://127.0.0.1:8000/programadores/](http://127.0.0.1:8000/programadores/)
- **Endpoint DRF Puro:** [http://127.0.0.1:8000/api/programmers/](http://127.0.0.1:8000/api/programmers/)
- **Panel Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Usuario:** `profe`
  - **Contraseña:** `123456`

---

## 🧪 Ejecutar Pruebas Automatizadas

```powershell
py manage.py test
```
