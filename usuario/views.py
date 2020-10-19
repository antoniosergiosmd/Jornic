from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registrar.html'
    success_url = reverse_lazy('login')

def UserPerfil(request):
    template_name = 'registration/perfil_usuario.html'
    context = {
        'perfil': 'perfil',
    }
    return render(request, template_name, context)

