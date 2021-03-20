from django import forms
from .models import usuarios


class usuariosForm(forms.ModelForm):
    """Form definition for usuarios."""

    class Meta:
        """Meta definition for usuariosform."""

        model = usuarios
        fields = ("nombre","apellido","correo","password","fecha_nacimiento")
