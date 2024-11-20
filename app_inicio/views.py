from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from app_juegos.forms import UsuarioForm
from app_juegos.models import Usuario, Puntuacion

# Create your views here.
def index(request):
    return render(request, 'app_inicio/index.html')

def deforestacion(request):
    return render(request, 'app_inicio/deforestacion.html')

def contaminacionAgua(request):
    return render(request, 'app_inicio/contaminacionAgua.html')

def contaminacionAire(request):
    return render(request, 'app_inicio/contaminacionAire.html')

def recursosNaturales(request):
    return render(request, 'app_inicio/recursosNaturales.html')

def usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            if Usuario.objects.filter(nombre=nombre).exists():
                form.add_error('nombre', 'El nombre de usuario ya existe. Por favor, elige otro.')
            else:
                usuario = form.save()
                # Crear puntuaciones por defecto para el nuevo usuario
                Puntuacion.objects.create(usuario=usuario, quiz=0)
                # Guardar el nombre de usuario en la sesión
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('menu')  # Redirigir al menú del jugador
    else:
        form = UsuarioForm()
    return render(request, 'app_inicio/juegos.html', {'form': form})

def about(request):
    return render(request, 'app_inicio/about.html')
