from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts.views import SignUpView, InicioView # Actualizado

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    # Nueva ruta para la página de inicio
    path("inicio/", InicioView.as_view(), name="inicio"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
