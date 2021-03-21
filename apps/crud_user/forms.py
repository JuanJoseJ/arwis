from django import forms
from .models import usuarios
import datetime


class usuariosForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }),
        input_formats=('%m/%d/%Y', ),
    )

    class Meta:
        model = usuarios
        fields = ("nombre", "apellido", "correo",
                  "password", "fecha_nacimiento")


class loginForm(forms.Form):

    correo = forms.EmailField(
        widget=forms.EmailInput()
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = usuarios
        fields = ("correo", "password")
