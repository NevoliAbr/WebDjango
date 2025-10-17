"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de Autenticación y Públicas
    path('', views.inicio, name='inicio'), # Página principal (Buscador público o Dashboard)
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('registro/', views.register, name='register'),

    # Rutas de la aplicación (protegidas por @login_required en las vistas)
    path('agregar/', views.agregar_moto, name='agregar'),
    path('terminar/<int:moto_id>/', views.terminar_trabajo, name='terminar_trabajo'), # Corregido para aceptar enteros
    path('consulta/', views.consulta, name='consulta'),
]

# Servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
