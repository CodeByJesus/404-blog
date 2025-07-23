from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout # Importa la función logout
from django.contrib import messages # Importa el módulo messages
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(auth_views.LoginView):
    def form_valid(self, form):
        # Llama al método form_valid de la clase padre para realizar el login
        response = super().form_valid(form)
        
        # Verifica si el usuario autenticado es un superusuario
        if self.request.user.is_superuser:
            # Si es superusuario, y no está iniciando sesión desde /admin/
            if not self.request.path.startswith('/admin/'):
                logout(self.request) # Cierra la sesión del superusuario
                messages.error(self.request, "Los superusuarios solo pueden iniciar sesión desde el panel de administración.")
                return redirect('login') # Redirige de vuelta a la página de login
        return response