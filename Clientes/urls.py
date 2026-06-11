from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.iniciar_sesion, name="iniciar_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
    path("registro/", views.registro, name="registro"),
    path("recuperar/", views.recuperar_contrasena, name="recuperar_contrasena"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]