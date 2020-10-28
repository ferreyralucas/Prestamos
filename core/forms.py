from django import forms
from .models import Prestamo

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('dni', 'nombre', 'apellido', 'genero','email','monto')
        labels = {
            "dni":"DNI",
            "nombre":"Nombre",
            "apellido":"Apellido",
            "genero":"Genero",
            "email":"Email",
            "monto":"Monto solicitado"

        }
    def clean(self):
        self.cleaned_data.get("dni")
