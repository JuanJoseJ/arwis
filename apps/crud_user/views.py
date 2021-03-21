from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import usuariosForm, loginForm
from .models import usuarios
from datetime import date
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.

# vista para la creación de usuarios


class usuario_crear(FormView):
    template_name = "user/usuario_crear.html"
    form_class = usuariosForm
    success_url = reverse_lazy('user:login')

    # valido la info
    def form_valid(self, form):
        # traigo los datos
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        password = form.cleaned_data['password']
        fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

        # verifico si el nombre NO contiene numeros
        if not any(i.isdigit() for i in nombre):
            # verifico si el nombre NO contiene numeros
            if not any(i.isdigit() for i in apellido):
                # verifico que la contraseña contenga por lo menos un numero
                if any(i.isdigit() for i in password):
                    # miro que el usuario tenga por lo menos 18 años
                    # la fn de la edad me trae, la diferencia en años, y le resta uno si la fecha de cumpleaños no ha pasado 0 o 1
                    edad = date.today().year - fecha_nacimiento.year - ((date.today().month,
                                                                         date.today().day) < (fecha_nacimiento.month, fecha_nacimiento.day))
                    if edad >= 18:
                        # verifico todo, y si pasa, creo el usuario
                        user = usuarios.objects.create_user(
                            form.cleaned_data['nombre'],
                            form.cleaned_data['apellido'],
                            form.cleaned_data['password'],
                            form.cleaned_data['correo'],
                            form.cleaned_data['fecha_nacimiento'],
                        )
                        print(user.get_username())

        return super(usuario_crear, self).form_valid(form)


class usuario_login(FormView):
    template_name = "user/usuario_login.html"
    form_class = loginForm
    success_url = reverse_lazy('user:crear')

    def form_valid(self, form):
        print(form.cleaned_data['correo'])
        usuario = authenticate(
            self.request, 
            username=form.cleaned_data['correo'], 
            password=form.cleaned_data['password']
        )
        print(usuario)
        if usuario is not None:
            login(self.request, usuario)
        else:
            print(
                '-------------------------------NOOOOO----------------------------------------')
            return HttpResponseRedirect(
                reverse_lazy('user:login')
            )

        return super(usuario_login, self).form_valid(form)
