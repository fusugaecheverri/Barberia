from django.shortcuts import render, redirect
from django.core.mail import send_mail

def ver_contactanos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        # Correo al dueño
        send_mail(
            subject=f'Nuevo mensaje de {nombre}',
            message=f'Nombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}\n\nMensaje:\n{mensaje}',
            from_email='fusugaecheverri@gmail.com',
            recipient_list=['fusugaecheverri@gmail.com'],
        )

        # Correo al cliente
        send_mail(
            subject='Recibimos tu mensaje - 1312 Barber Club',
            message=f'Hola {nombre},\n\nHemos recibido tu mensaje y te contactaremos pronto.\n\n1312 Barber Club',
            from_email='fusugaecheverri@gmail.com',
            recipient_list=[correo],
        )

        return redirect('contactanos_exitoso')

    return render(request, 'contactanos.html')

def contactanos_exitoso(request):
    return render(request, 'contactanos_exitoso.html')
