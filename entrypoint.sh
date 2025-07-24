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
exec "$@"
