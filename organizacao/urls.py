from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import org_view

from django.conf.urls.static import static
app_name = 'organizacao'
urlpatterns = [
    path('organizacao/', org_view, name='org_page')

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )