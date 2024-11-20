from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, newContraseñaForm
from django.db.models import Count, Q, Avg
from .models import Pregunta, Respuesta
from app_juegos.models import Puntuacion

@login_required(login_url='adminLogin')
def administrador(request):
    username = request.session.get('username')
    if not  username:
        return redirect('adminLogin')
    
    total = Puntuacion.objects.count()
    mal = Puntuacion.objects.filter(quiz__lte=5).count()
    mas_o_menos = Puntuacion.objects.filter(quiz__gt=5, quiz__lte=10).count()
    bien = Puntuacion.objects.filter(quiz__gt=10, quiz__lte=15).count()
    excelente = Puntuacion.objects.filter(quiz__gt=15, quiz__lte=20).count()
    
    # Calcular los porcentajes
    mal_pct = (mal / total * 100) if total > 0 else 0
    mas_o_menos_pct = (mas_o_menos / total * 100) if total > 0 else 0
    bien_pct = (bien / total * 100) if total > 0 else 0
    excelente_pct = (excelente / total * 100) if total > 0 else 0

    data = {
        'mal': mal,
        'mal_pct': mal_pct,
        'mas_o_menos': mas_o_menos,
        'mas_o_menos_pct': mas_o_menos_pct,
        'bien': bien,
        'bien_pct': bien_pct,
        'excelente': excelente,
        'excelente_pct': excelente_pct
    }

    return render(request, 'app_administrador/index.html', {'username':username, 'data': data})

@login_required(login_url='adminLogin')
def adminLogout(request):
    logout(request)
    return redirect('adminLogin')

@login_required(login_url='adminLogin')
def register(request):
    username = request.session.get('username')
    if not  username:
        return redirect('adminLogin')    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('administrador')
    else:
        form = RegisterForm()
    return render(request, 'app_administrador/register.html', {'form': form, 'username': username})

@login_required(login_url='adminLogin')
def newPassword(request):
    username = request.session.get('username')
    if not  username:
        return redirect('adminLogin')
    
    if request.method == 'POST':
        form = newContraseñaForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            user = authenticate(username=request.user.username, password=old_password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Esto mantiene la sesión del usuario después de cambiar la contraseña
                return redirect('administrador')
            else:
                return render(request, 'app_administrador/cambiarContraseña.html', {'form': form, 'error': 'La contraseña actual no es correcta.'})
    else:
        form = newContraseñaForm()
    return render(request, 'app_administrador/cambiarContraseña.html', {'form': form, 'username': username})

def estadisticas(request):
    username = request.session.get('username')
    if not  username:
        return redirect('adminLogin')
    
    preguntas = Pregunta.objects.annotate(
        total_respuestas=Count('respuesta'),
        correctas=Count('respuesta', filter=Q(respuesta__correcta=True)),
        tiempo_promedio=Avg('respuesta__tiempo_respuesta')
    )

    data = {
        'labels': [pregunta.texto for pregunta in preguntas],
        'total_respuestas': [pregunta.total_respuestas for pregunta in preguntas],
        'correctas': [pregunta.correctas for pregunta in preguntas],
        'porcentajes': [
            (pregunta.correctas / pregunta.total_respuestas) * 100 if pregunta.total_respuestas > 0 else 0
            for pregunta in preguntas
        ],
        'tiempo_promedio': [pregunta.tiempo_promedio or 0 for pregunta in preguntas]  # Asegurar que no haya valores nulos
    }

    context = {'data': data, 'username': username}
    return render(request, 'app_administrador/estadisticas.html', context)

@login_required(login_url='adminLogin')
def tablas(request):
    username = request.session.get('username')
    if not  username:
        return redirect('adminLogin')
    
    preguntas = Pregunta.objects.annotate(
        total_respuestas=Count('respuesta'),
        correctas=Count('respuesta', filter=Q(respuesta__correcta=True))
    )
    
    for pregunta in preguntas:
        if pregunta.total_respuestas > 0:
            pregunta.porcentaje_correctas = (pregunta.correctas / pregunta.total_respuestas) * 100
        else :
            pregunta.porcentaje_correctas = 0
            
    context={'preguntas': preguntas, 'username': username}
    return render(request, 'app_administrador/tablas.html', context)