# Mi Blog (Backend)

¡Bienvenido al repositorio del **backend** de mi blog personal! Este proyecto es una aplicación web desarrollada con Django que gestiona el contenido de los posts, categorías, etiquetas y usuarios.

**Nota Importante sobre el Despliegue:**
Debido a las limitaciones y costos asociados con el despliegue continuo de aplicaciones full-stack (backend + frontend) en plataformas gratuitas como Render, Railway, etc., la versión pública de este blog ahora utiliza una arquitectura separada:

*   **Frontend Estático (Blog Público):** El contenido del blog se genera como un sitio estático usando [Pelican](https://getpelican.com/) y se despliega en [Netlify](https://www.netlify.com/). Esto proporciona un blog rápido, seguro y económico. Puedes ver el código fuente de este frontend estático aquí: [github.com/CodeByJesus/404-blog-estatico](https://github.com/CodeByJesus/404-blog-estatico)
*   **Backend (este repositorio):** Este proyecto ahora sirve principalmente como el sistema de gestión de contenido (CMS) para el blog estático. Su propósito es permitir la creación, edición y eliminación de posts a través del panel de administración de Django, y está diseñado para ser ejecutado localmente para fines de desarrollo y gestión de contenido.

## 🚀 Características (Backend)

*   **Gestión de Posts:** Creación, edición y eliminación de entradas de blog.
*   **Categorías y Etiquetas:** Organización de contenido.
*   **Editor de Texto Enriquecido:** (TinyMCE) para el contenido de los posts.
*   **Panel de Administración de Django:** Interfaz para la gestión de contenido.
*   **Internacionalización (i18n):** Soporte para múltiples idiomas en el backend.

## 🛠️ Tecnologías Utilizadas (Backend)

Este proyecto ha sido construido utilizando las siguientes tecnologías:

**Backend & Framework:**
*   **Python:** Lenguaje de programación principal.
*   **Django:** Framework web de alto nivel para un desarrollo rápido y seguro.
*   **Django REST Framework:** (Si aplica, para futuras APIs de contenido).
*   **Gunicorn:** Servidor WSGI (si se desplegara el backend).
*   **psycopg2-binary:** Adaptador para la conexión con bases de datos PostgreSQL.
*   **dj-database-url:** Para gestionar la configuración de la base de datos a través de URLs de entorno.
*   **django-environ:** Para la gestión de variables de entorno.
*   **Whitenoise:** Para servir archivos estáticos de Django (si se desplegara el backend).
*   **django-tinymce:** Editor de texto enriquecido.

**Base de Datos:**
*   **PostgreSQL:** Base de datos relacional (si se desplegara el backend).
*   **SQLite:** Base de datos ligera utilizada para desarrollo local.

**Herramientas:**
*   **Git:** Sistema de control de versiones.
*   **GitHub:** Plataforma para el alojamiento del código fuente.

## ⚙️ Configuración y Ejecución Local (Solo Backend)

Sigue estos pasos para configurar y ejecutar el **backend** de este proyecto en tu máquina local. Esto te permitirá gestionar el contenido del blog a través del panel de administración de Django.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/CodeByJesus/404-blog.git # Reemplaza con la URL de tu repositorio de blog
    cd mi_blog
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\\Scripts\\activate   # En Windows
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la base de datos local:**
    Asegúrate de que no exista un archivo `db.sqlite3` en la raíz del proyecto. Si existe, bórralo.
    ```bash
    rm db.sqlite3 # En Linux/macOS
    # del db.sqlite3 # En Windows
    ```
    Luego, aplica las migraciones para crear la base de datos y las tablas:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crear un superusuario (para acceder al panel de administración):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear tu usuario y contraseña.

6.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El **backend** de la aplicación estará disponible en `http://127.0.0.1:8000/`. Puedes acceder al panel de administración en `http://127.0.0.1:8000/admin/`.

## 🌐 Despliegue en Producción

La versión pública de este blog utiliza un **frontend estático** generado con Pelican y desplegado en Netlify. Este repositorio sirve como el CMS para gestionar el contenido que luego se exporta a Markdown para el sitio estático.

### Versión Funcional del Blog (Estática)

La versión completamente funcional y accesible públicamente de este blog es la **versión estática**, desplegada en Netlify. Esta versión es extremadamente rápida, segura y económica de mantener.

*   **URL del Blog Estático:** [https://TU_URL_NETLIFY_BLOG.netlify.app](https://TU_URL_NETLIFY_BLOG.netlify.app) (Reemplaza con la URL real de tu blog en Netlify)
*   **Código Fuente del Frontend Estático:** [https://github.com/CodeByJesus/404-blog-estatico](https://github.com/CodeByJesus/404-blog-estatico)

**Limitaciones de la Versión Estática:**
Es importante entender que, al ser un sitio estático, esta versión no incluye funcionalidades dinámicas que requieren un backend en tiempo real, como:
*   Sistema de comentarios.
*   Funcionalidad de búsqueda en el sitio (a menos que se implemente con JavaScript en el cliente).
*   Autenticación de usuarios o cualquier interacción con una base de datos en vivo.

Para la gestión de contenido y el desarrollo de estas funcionalidades dinámicas, se debe utilizar la versión backend de este repositorio, ejecutándola localmente.

## 🌍 Internacionalización (i18n)

El backend de la aplicación soporta múltiples idiomas para la gestión de contenido.

---
