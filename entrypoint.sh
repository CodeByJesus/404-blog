#!/bin/sh

# Salir inmediatamente si un comando falla
set -e

# Limpiar archivos de bytecode de Python para evitar problemas de caché
echo "Limpiando archivos .pyc..."
find . -name "*.pyc" -delete

# Aplicar las migraciones de la base de datos
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

# Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
# Ignora el comando pasado y ejecuta gunicorn directamente,
# usando la variable de entorno PORT que proporcionan plataformas como Railway/Render.
exec gunicorn mi_blog.wsgi:application --bind 0.0.0.0:${PORT:-8000}
