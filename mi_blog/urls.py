from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView # Importa tu vista de login personalizada

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')), # URLs de TinyMCE
    path('', include('posts.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'), # Usa tu vista de login personalizada
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_admin_only.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('users.urls')), # URLs de la aplicación de usuarios
    prefix_default_language=True
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Sirve archivos estáticos en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)