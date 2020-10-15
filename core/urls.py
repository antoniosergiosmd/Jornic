from django.contrib import admin
from django.urls import path
from core.views import home , login

app_name = 'core'

urlpatterns = [
    path('', home , name = 'home_page'),
    path('login', login , name = 'login_page')
]
