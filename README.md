# 🌤️ App Climática

Aplicación de gestión y registro del clima.

---

## 📁 Estructura del proyecto

```
weather-app/
├── controller/
│   ├── control_alert.py         # Controlador de alertas
│   ├── control_menu.py          # Controlador del menú
│   └── control_time.py          # Controlador de tiempo/fechas
├── data/
│   └── register.json            # Almacenamiento de registros
├── model/
│   ├── manager.py               # Gestor principal de datos
│   └── register_weather.py      # Modelo de registro del clima
├── test/
│   ├── test_control_alert.py    # Tests del controlador de alertas
│   ├── test_control_weather.py  # Tests del controlador del clima
│   ├── test_index.py            # Tests del punto de entrada
│   ├── test_manager.py          # Tests del gestor
│   └── test_register_weather.py # Tests del modelo de clima
├── view/
│   └── menu.py                  # Vista del menú principal
└── index.py                     # Punto de entrada de la aplicación
```

---

## 🚀 Descargar Repo

```bash
# Clonar el repositorio
git clone git@github.com:lermns/App_climatica_Python.git
```

---

## 📝 Guía de Conventional Commits

Usa esta guía para elegir el tipo correcto en cada commit:

```
¿Corregiste un error o bug?
  Sí → fix:
  No ↓

¿Cambiaste funcionalidad existente o afectaste la interfaz de usuario?
  Sí → feat:
  No ↓

¿Añadiste o modificaste tests?
  Sí → test:
  No ↓

¿Cambiaste el estilo o formato del código (sin afectar su comportamiento)?
  Sí → style:
  No ↓

¿Realizaste cambios en la documentación?
  Sí → docs:
  No ↓

¿Modificaste la forma en que se construye el proyecto (paquetes, dependencias, dockerfile, etc.)?
  Sí → build:
  No ↓

¿Cambiaste algo relacionado con DevOps (pipelines de CI/CD, despliegue, etc.)?
  Sí → ops:
  No ↓

¿Completaste una tarea de mantenimiento o no relacionada con el código (ej. .gitignore, commit inicial)?
  Sí → chore:
  No ↓

¿Reescribiste o reestructuraste código específicamente para mejorar el rendimiento?
  Sí → perf:
  No → refactor:
```

### Formato de un commit

```
<tipo>(<ámbito opcional>): <descripción breve>
```

### Ejemplos

| Commit | Cuándo usarlo |
|---|---|
| `fix(alert): corregir umbral de temperatura` | Se corrige un bug en las alertas |
| `feat(menu): añadir opción de exportar datos` | Se añade una nueva funcionalidad |
| `test(manager): añadir tests unitarios` | Se crean o modifican tests |
| `style: aplicar formato PEP8` | Cambios de estilo sin lógica |
| `docs: actualizar README` | Cambios en documentación |
| `build: añadir dependencia requests` | Cambios en dependencias |
| `ops: configurar pipeline de CI` | Cambios en CI/CD |
| `chore: añadir .gitignore` | Tareas de mantenimiento |
| `perf(manager): optimizar lectura de JSON` | Mejora de rendimiento |
| `refactor(controller): simplificar lógica` | Refactorización sin cambio de comportamiento |
