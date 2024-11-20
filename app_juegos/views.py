from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Usuario, Puntuacion
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_administrador.models import Pregunta, Respuesta

def menu(request):
    usuario_nombre = request.session.get('usuario_nombre')
    if not usuario_nombre:
        return redirect('usuario')
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    puntuacion = Puntuacion.objects.get(usuario=usuario)
    context = {
        'usuario': usuario,
        'puntuacion': puntuacion
    }
    return render(request, 'app_juegos/menu.html', context)

@csrf_exempt
def quiz(request):
    usuario_nombre = request.session.get('usuario_nombre')
    if not usuario_nombre:
        return redirect('usuario')
    
    if request.method == 'POST':
        cantidad_acertadas = request.POST.get('cantidadAcertadas')
        respuestas = request.POST.get('respuestas').split('|')
        
        print("Nombre de Usuario:", usuario_nombre)
        print("Cantidad Acertadas:", cantidad_acertadas)
        print("Respuestas:", respuestas)
        
        try:
            usuario = Usuario.objects.get(nombre=usuario_nombre)
            puntuacion, created = Puntuacion.objects.get_or_create(usuario=usuario)
            puntuacion.quiz = cantidad_acertadas
            puntuacion.save()
            
            for respuesta in respuestas:
                if ',' in respuesta:
                    partes = respuesta.split(',')
                    if len(partes) == 3:
                        pregunta_id, correcta, tiempo_respuesta = partes
                        tiempo_respuesta = float(tiempo_respuesta)
                    else:
                        pregunta_id, correcta = partes
                        tiempo_respuesta = 0.0
                    
                    if pregunta_id.isnumeric():
                        try:
                            pregunta = Pregunta.objects.get(id=pregunta_id)
                            correcta = True if correcta.lower() == 'true' else False
                            if not Respuesta.objects.filter(pregunta=pregunta, usuario=usuario).exists():
                                Respuesta.objects.create(
                                    pregunta=pregunta,
                                    correcta=correcta,
                                    usuario=usuario,
                                    tiempo_respuesta=tiempo_respuesta
                                )
                        except Pregunta.DoesNotExist:
                            print(f"pregunta con id {pregunta_id} no encontrada")
            return redirect('puntuacion')
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado."}, status=400)
    return render(request, 'app_juegos/quiz.html')



def puntuacion(request):
    usuario_nombre = request.session.get('usuario_nombre')
    if not usuario_nombre:
        return redirect('usuario')
    
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    puntuaciones_quiz = Puntuacion.objects.all().order_by('-quiz')
    context = {
        'usuario': usuario,
        'puntuaciones_quiz': puntuaciones_quiz,
    }
    return render(request, 'app_juegos/puntuacion.html', context)

def adminLogin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return redirect('administrador')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'app_juegos/adminLogin.html', {'form': form})