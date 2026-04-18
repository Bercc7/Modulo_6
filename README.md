TaskMaster Django 🚀

TaskMaster es una plataforma web robusta diseñada para la gestión eficiente de proyectos y tareas. Desarrollada con el framework Django, la aplicación ofrece un entorno seguro y escalable donde los usuarios pueden organizar sus flujos de trabajo de manera dinámica.
🎯 Propósito del Proyecto

El objetivo fue integrar diversos módulos de Django para crear una herramienta funcional que resuelva la necesidad de administración de proyectos en equipos tecnológicos, garantizando la seguridad en el acceso y la integridad de los datos.
Funcionalidades Principales:

    Sistema de Autenticación Completo: Registro, inicio y cierre de sesión utilizando django.contrib.auth.

    Gestión de Proyectos y Tareas: Creación, edición y eliminación (CRUD) de proyectos con relaciones personalizadas entre usuarios y sus tareas.

    Seguridad Avanzada: Restricciones de acceso mediante LoginRequiredMixin y protección robusta contra ataques CSRF en todos los formularios.

    Panel Administrativo Personalizado: Interfaz de administración de Django configurada para una gestión eficiente de usuarios, permisos y modelos.

    Interfaz Dinámica: Uso de herencia de plantillas (Templates) para una navegación fluida y modular.

🛠️ Stack Tecnológico

    Backend: Python 3 & Django Framework (v5.2).

    Frontend: Django Templates con lógica de contextos dinámicos.

    Base de Datos: SQLite (desarrollo) / Compatible con PostgreSQL (producción).

    Formularios: Implementación de forms.ModelForm con validaciones personalizadas en el servidor.

📐 Arquitectura y Diseño

El proyecto sigue el patrón MVT (Model-View-Template) de Django para asegurar una separación clara de responsabilidades:

    Modelos: Definición de relaciones "Uno a Muchos" entre usuarios y tareas.

    Vistas: Lógica basada en clases (CBVs) para un código más limpio y reutilizable.

    Seguridad: Validación de datos estricta antes de la persistencia en la base de datos.

⚙️ Instalación y Configuración

Para desplegar el proyecto localmente, sigue estos pasos:

    Clona el repositorio:
    Bash

    git clone https://github.com/Bercc7/Task-Manager-Django.git
    Crea y activa un entorno virtual:
    Bash

    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

    Instala las dependencias:
    Bash

    pip install -r requirements.txt

    Realiza las migraciones:
    Bash

    python manage.py migrate

    Inicia el servidor:
    Bash

    python manage.py runserver
