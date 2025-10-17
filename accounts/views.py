from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta

from .forms import MotoForm
from .models import Moto

# --- Vistas de Autenticación ---

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso!")
            return redirect('inicio')
        else:
            error_list = [error for field in form.errors.values() for error in field]
            messages.error(request, f"Error en el registro: {error_list[0]}")

    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')

# --- Vistas de la Aplicación ---

def inicio(request):
    # Si el usuario está autenticado, muestra el dashboard de siempre
    if request.user.is_authenticated:
        todas_las_motos = Moto.objects.all()
        motos_activas = [moto for moto in todas_las_motos if moto.activo]
        return render(request, "inicio.html", {"lista_motos": motos_activas})
    
    # Si el usuario no está autenticado, funciona como buscador público
    else:
        moto_encontrada = None
        query_id = request.GET.get('moto_id')

        if query_id:
            try:
                moto_encontrada = Moto.objects.get(id=query_id)
            except (Moto.DoesNotExist, ValueError):
                messages.error(request, f'No se encontró ninguna moto con el ID "{query_id}". Por favor, verifica el número.')
        
        return render(request, "inicio.html", {'moto_encontrada': moto_encontrada})


@login_required
def terminar_trabajo(request, moto_id):
    moto = get_object_or_404(Moto, id=moto_id)
    moto.activo = False
    moto.save(update_fields=['activo'])
    messages.success(request, f'El trabajo para la moto {moto.modelo} se ha marcado como finalizado.')
    return redirect('inicio')

@login_required
def agregar_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Moto agregada correctamente!')
            return redirect('inicio')
        else:
            print("\n--- ERRORES DEL FORMULARIO ---")
            print(form.errors.as_json())
            print("----------------------------\n")
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = MotoForm()
    return render(request, 'agregar.html', {'form': form})

@login_required
def consulta(request):
    rango = request.GET.get('rango', 'mes')
    today = date.today()

    todas_las_motos = Moto.objects.all()
    motos_filtradas = []

    if rango == 'hoy':
        start_date = today
    elif rango == 'semana':
        start_date = today - timedelta(days=today.weekday())
    elif rango == 'mes':
        start_date = today.replace(day=1)
    else:
        rango = 'mes'
        start_date = today.replace(day=1)

    for moto in todas_las_motos:
        if moto.fecha_inicio_trabajo and moto.fecha_inicio_trabajo >= start_date:
            motos_filtradas.append(moto)

    context = {
        'lista_motos': motos_filtradas,
        'rango_seleccionado': rango,
    }
    return render(request, "consulta.html", context)
