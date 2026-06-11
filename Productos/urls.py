from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ver_Productos, name='Productos'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)