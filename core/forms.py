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
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    "class":"form-control",
                    "placeholder":"Ingrese el DNI"
                }
            )
        }

class EditSolicitudForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('dni', 'nombre', 'apellido', 'genero','email','monto','aprobado')
        labels = {
            "dni":"DNI",
            "nombre":"Nombre",
            "apellido":"Apellido",
            "genero":"Genero",
            "email":"Email",
            "monto":"Monto solicitado",
            "aprobado":"Aprobado"

        }
