# /home/jesus/blog-proyecto/mi_blog/mi_blog/admin_cookie_middleware.py
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.models import Session

class AdminCookieMiddleware(SessionMiddleware):
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            # Usar un nombre de cookie diferente para el admin
            settings.SESSION_COOKIE_NAME = 'admin_sessionid'
        else:
            # Usar el nombre de cookie predeterminado para el resto del sitio
            settings.SESSION_COOKIE_NAME = 'sessionid' # O el nombre que uses para el blog

        # Llamar al método original de SessionMiddleware para procesar la sesión
        super().process_request(request)

    def process_response(self, request, response):
        # Asegurarse de que la cookie se establezca con el nombre correcto
        if request.path.startswith('/admin/') and request.session.session_key:
            response.set_cookie(
                settings.SESSION_COOKIE_NAME,
                request.session.session_key,
                max_age=settings.SESSION_COOKIE_AGE,
                expires=None, # O la fecha de expiración que desees
                domain=settings.SESSION_COOKIE_DOMAIN,
                path=settings.SESSION_COOKIE_PATH,
                secure=settings.SESSION_COOKIE_SECURE,
                httponly=settings.SESSION_COOKIE_HTTPONLY,
                samesite=settings.SESSION_COOKIE_SAMESITE,
            )
        return super().process_response(request, response)
