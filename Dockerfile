# Usa una imagen base de Python mรกs reciente (Bullseye) para evitar problemas con repositorios antiguos
FROM python:3.9-slim-bullseye

# Establece variables de entorno para un entorno de contenedor mรกs limpio
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las herramientas de gettext, necesarias para las traducciones de Django
RUN apt-get update && apt-get install -y gettext

# Copia el archivo de requerimientos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el cรณdigo del proyecto al directorio de trabajo
COPY . .

# Proporciona una clave secreta temporal solo para el proceso de build
# La clave real se proporcionarรก en tiempo de ejecuciรณn a travรฉs de variables de entorno
ARG DJANGO_SECRET_KEY=a-dummy-secret-key-for-build-time

# Ejecuta collectstatic para reunir todos los archivos estรกticos
# Se necesitan varias variables de entorno para que este comando se ejecute
# Se usan valores ficticios que solo son vรกlidos durante la construcciรณn de la imagen
RUN SECRET_KEY=$DJANGO_SECRET_KEY ALLOWED_HOSTS='*' DATABASE_URL='sqlite:////tmp/db.sqlite3' python manage.py collectstatic --noinput

# Copia el script de entrypoint y lo hace ejecutable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expone el puerto en el que se ejecutarรก la aplicaciรณn
EXPOSE 8000

# Establece el script de entrypoint que se ejecutarรก al iniciar el contenedor
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando por defecto que se pasarรก al entrypoint
# El entrypoint lo ejecutarรก con `exec "$@"`
# El entrypoint lo ejecutará con `exec "$@"`.
# Escucha en el puerto proporcionado por la variable de entorno PORT, con 8000 como valor por defecto.
# Se usa la forma "shell" de CMD para que la variable $PORT se expanda correctamente.
CMD []
