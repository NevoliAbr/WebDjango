from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm

# Vista para el registro de usuarios
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Vista para la página de inicio (después del login)
class InicioView(TemplateView):
    template_name = "inicio.html"
