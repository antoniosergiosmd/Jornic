from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView, UserPerfil

app_name = 'usuario'

urlpatterns = [
    path('registrar/', UserRegisterView.as_view(), name='registrar'),
    path('perfil/', UserPerfil, name='perfil')
]