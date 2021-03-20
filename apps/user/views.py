from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import usuariosForm

# Create your views here.


class usuario_crear(FormView):
    template_name = "sessions/usuario_crear.html"
    form_class = usuariosForm
    success_url = "users/log-in"
