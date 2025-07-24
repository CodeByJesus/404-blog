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
# Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."

# Validar y establecer la variable PORT
if ! [[ "$PORT" =~ ^[0-9]+$ ]]; then
  echo "Advertencia: La variable PORT no es un número válido o está vacía. Usando el puerto por defecto 8000."
  PORT=8000
fi

# Ignora el comando pasado y ejecuta gunicorn directamente,
# usando la variable de entorno PORT que proporcionan plataformas como Railway/Render.
echo "Valor de PORT recibido: $PORT"
exit 1 # Salir para que podamos ver el valor en los logs
