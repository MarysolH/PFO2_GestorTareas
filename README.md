# PFO 2 – Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto implementa un **servidor Flask con SQLite** que permite:  
- Registro de usuarios  
- Inicio de sesión con contraseñas hasheadas  
- Visualización de una página de bienvenida a las tareas  

Además, incluye un **cliente en consola** que interactúa con la API.

---

## Tecnologías utilizadas
- Python 3
- Flask (API REST)
- SQLite (base de datos)
- Werkzeug (hash de contraseñas)
- Requests (para el cliente en consola)

---

## Estructura del proyecto

PFO2_gestorTareas/
│
├── servidor.py # Servidor Flask (endpoints)
├── db.py # Funciones de base de datos
├── cliente.py # Cliente en consola (interacción con la API)
├── database.db # Base de datos SQLite (se crea al ejecutar)
├──capturas/ #registro, login, tareas.
└── README.md # Documentación

## Instalación y ejecución

1. **Clonar el repositorio**   
   ```
   git clone https://github.com/usuario/PFO2_GestionTareas.git
   cd PFO2_GestionTareas 
2. **Instalar dependencias**  
```pip install flask requests```

3. **Ejecutar el servidor**  
``` python servidor.py ```

4. **Abrir otra terminal y ejecutar el cliente**  
```python cliente.py```

5. **Probar funcionalidades**
- Registrar un usuario
- Iniciar sesión
- Ver tareas en http://127.0.0.1:5000/tareas

6. **Pruebas exitosas**


## Respuestas conceptuales
1. ¿Por qué hashear contraseñas?
Las contraseñas nunca deben almacenarse en texto plano porque, en caso de que la base de datos sea comprometida, los atacantes tendrían acceso directo a las credenciales. Al aplicar un algoritmo de hash seguro (ej. Werkzeug/Hash), se guarda únicamente el resultado encriptado, lo que protege la información del usuario.

2. Ventajas de usar SQLite en este proyecto
- Es ligero y no requiere configuración de servidor externo.
- Perfecto para proyectos educativos, prototipos o sistemas pequeños.
- Almacena los datos en un único archivo (database.db), facilitando el despliegue y portabilidad.
- Es compatible con Python de forma nativa.

## GitHub Pages
La docunmentación y capturas disponibles en 