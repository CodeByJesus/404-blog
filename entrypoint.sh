#!/bin/sh
set -e

# Si se pasan argumentos al script (desde 'railway run', por ejemplo),
# ejecutar esos argumentos como un comando.
if [ "$#" -gt 0 ]; then
  exec "$@"
fi

# Si no se pasan argumentos, ejecutar el proceso de inicio por defecto del servidor.
# Aplicar las migraciones de la base de datos
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

# Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
PORT="${PORT:-8000}"
exec gunicorn mi_blog.wsgi:application --bind 0.0.0.0:$PORT