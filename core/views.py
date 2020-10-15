from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template_name = 'index.html'
    context = {
        'core': 'core',
    }
    return render(request, template_name, context)


def login(request):
    template_name = 'login.html'
    context = {
        'core': 'core',
    }
    return render(request, template_name, context)