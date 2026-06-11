from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Barbas/', views.ver_Barbas, name='Barbas'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)