#!/bin/sh
set -e

# Si se pasan argumentos al script (como desde 'railway run'),
# los ejecuta. Esto es útil para comandos de mantenimiento.
if [ "$#" -gt 0 ]; then
  exec "$@"
fi

# Si no se pasan argumentos, ejecuta el proceso de inicio por defecto.
# Aplica las migraciones de la base de datos.
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

# Inicia el servidor Gunicorn.
echo "Iniciando Gunicorn..."
PORT="${PORT:-8000}"
exec gunicorn mi_blog.wsgi:application --bind 0.0.0.0:$PORT