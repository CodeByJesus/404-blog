# /home/jesus/blog-proyecto/mi_blog/mi_blog/admin_session_middleware.py
from django.conf import settings
from django.utils.module_loading import import_string

class AdminSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Guarda el motor de sesión original
            original_session_engine = settings.SESSION_ENGINE
            # Establece el motor de sesión para el admin
            settings.SESSION_ENGINE = 'mi_blog.admin_session_backend'
            # Carga la clase SessionStore del motor de sesión del admin
            SessionStore = import_string(settings.SESSION_ENGINE).SessionStore
            # Reemplaza el objeto de sesión en la solicitud
            request.session = SessionStore(request.session.session_key)

            response = self.get_response(request)

            # Restaura el motor de sesión original después de procesar la respuesta
            settings.SESSION_ENGINE = original_session_engine
            return response
        else:
            response = self.get_response(request)
            return response
