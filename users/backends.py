from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.sessions.models import Session

class SuperuserAdminOnlyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.is_superuser:
            # Si es un superusuario, solo permitir login desde el admin
            if request and request.path.startswith('/admin/'):
                authenticated_user = super().authenticate(request, username=username, password=password, **kwargs)
                if authenticated_user:
                    # Si la autenticación es exitosa, forzar una nueva sesión para el admin
                    # y establecer un nombre de cookie diferente
                    if request.session.session_key:
                        # Eliminar la sesión actual si existe para evitar conflictos
                        request.session.flush()

                    # Crear una nueva sesión con el nombre de cookie del admin
                    request.session = Session.objects.create()
                    request.session.set_expiry(0) # Expira al cerrar el navegador
                    request.session.save()

                    # Establecer el nombre de la cookie para el admin
                    # Esto se hará en el middleware, pero aquí aseguramos que la sesión esté lista
                    # para ser asociada con la cookie de admin.
                    # No podemos cambiar settings.SESSION_COOKIE_NAME aquí directamente
                    # porque es una configuración global.

                    return authenticated_user
                return None
            else:
                # No permitir login de superusuario desde el frontend
                return None
        else:
            # Para usuarios normales, usar el comportamiento por defecto
            return super().authenticate(request, username=username, password=password, **kwargs)

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None