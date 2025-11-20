Título del proyecto:
Autenticación JWT con FastAPI

Descripción general

Este proyecto implementa un sistema de autenticación basado en JSON Web Tokens (JWT) utilizando FastAPI. El objetivo es demostrar una arquitectura organizada, modular y coherente que permita gestionar registro, inicio de sesión y validación de usuarios de manera segura.

El proyecto está estructurado siguiendo buenas prácticas de desarrollo profesional, separando rutas, modelos, esquemas, servicios, configuración y conexión a base de datos. La intención es facilitar su lectura, mantenimiento y escalabilidad.

Tecnologías y librerías principales

Python 3.11+

FastAPI – Framework principal para la API.

Uvicorn – Servidor ASGI para desarrollo.

SQLite – Base de datos ligera para entorno académico.

SQLAlchemy – ORM para manejar las entidades y relaciones.

Pydantic – Validación de datos en solicitudes y respuestas.

Python-Jose – Generación y validación de JWT.

Passlib – Hashing seguro de contraseñas.

SQLite se seleccionó debido a:

Su facilidad de uso.

No requiere instalar servicios adicionales.

Permite concentrarse en la lógica de autenticación sin complejidad extra.

Estructura del proyecto

El código fuente vive dentro de la carpeta app/, organizado de la siguiente forma:

api/: Define las rutas expuestas por la API.

core/: Configuración central de la aplicación y funciones de seguridad (como JWT).

models/: Modelos de base de datos manejados con SQLAlchemy.

schemas/: Validaciones de datos mediante Pydantic.

services/: Lógica de negocio como login, registro y generación de tokens.

database.py: Configuración de la base de datos y creación de tablas.

main.py: Punto de entrada de la API.

Uso del archivo .env.example

El archivo .env.example contiene las variables necesarias para correr el proyecto (por ejemplo, la clave secreta para firmar JWT). El usuario debe duplicarlo y renombrarlo a .env antes de ejecutar la aplicación.

Activación del entorno virtual
python -m venv .venv
source .venv/Scripts/activate   # En Windows

Instalación de dependencias
pip install -r requirements.txt

Ejecución del servidor
uvicorn app.main:app --reload

Licencia
Este proyecto utiliza la licencia MIT, adecuada para proyectos educativos y demostrativos.