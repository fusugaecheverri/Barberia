from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

def registro(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST.get("email", "")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ese nombre de usuario ya está en uso.")
            return render(request, "registro.html")
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect("Principal")
    return render(request, "registro.html")

def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Principal")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, "login.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("Principal")

def recuperar_contrasena(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        nueva_password = request.POST.get("nueva_password")
        confirmar_password = request.POST.get("confirmar_password")
        try:
            user = User.objects.get(email=correo)
            if nueva_password and confirmar_password:
                if nueva_password == confirmar_password:
                    user.set_password(nueva_password)
                    user.save()
                    messages.success(request, "Contraseña cambiada exitosamente.")
                else:
                    messages.error(request, "Las contraseñas no coinciden.")
            else:
                messages.error(request, "Completa todos los campos.")
        except User.DoesNotExist:
            messages.error(request, "No existe una cuenta con ese correo.")
    return render(request, "recuperar_contrasena.html")