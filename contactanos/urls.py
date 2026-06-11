from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contactanos/', views.ver_contactanos, name='contactanos'),
    path('contactanos/exitoso/', views.contactanos_exitoso, name='contactanos_exitoso'),
] 