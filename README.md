# Mi Blog

Este es un proyecto de blog personal desarrollado con Django.

## Características

*   Creación, edición y eliminación de posts.
*   Comentarios en los posts.
*   Categorías y etiquetas para organizar los posts.
*   Soporte para múltiples idiomas (español e inglés).
*   Editor de texto enriquecido (TinyMCE) para el contenido de los posts.
*   Panel de administración de Django personalizado.

## Puesta en marcha (Desarrollo Local)

### Prerrequisitos

*   Python 3.8+
*   pip
*   virtualenv

### Instalación

1.  Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd mi_blog
    ```

2.  Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4.  Crea un archivo `.env` en la raíz del proyecto (`mi_blog/`) y añade las siguientes variables de entorno:
    ```
    SECRET_KEY='tu-secret-key-aqui'
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    DATABASE_URL=sqlite:///db.sqlite3
    ```

5.  Aplica las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

6.  Crea un superusuario para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

7.  Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Despliegue

Este proyecto está configurado para ser desplegado en Render. El archivo `render.yaml` contiene la configuración necesaria para el despliegue.
