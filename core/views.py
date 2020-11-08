import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolicitudForm, EditSolicitudForm
from .models import Prestamo
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView, ListView, UpdateView
from django.urls import reverse_lazy



class Inicio(TemplateView):
    template_name = "core/home.html"

class EditarPrestamo(UpdateView):
    model = Prestamo
    template_name = "core/form_pedir_prestamo.html"
    form_class = EditSolicitudForm
    success_url = reverse_lazy("/")

class ListarPrestamos(ListView):
    template_name = "core/tabla_prestamos.html"
    queryset = Prestamo.objects.all()
    context_object_name = "prestamos"

class PrestamosDeleteView(DeleteView):
    model = Prestamo
    success_url = '/prestamos/'

def solicitud_view(request):

    form_solicitud = SolicitudForm(request.POST or None)

    if request.POST:
        if form_solicitud.is_valid():
            form_solicitud.save()
            if request.POST.get("Create",True):
                form_solicitud= SolicitudForm()
            dni = request.POST.get('dni')
            if respuesta(dni)==True:
                prest = Prestamo.objects.filter(dni=dni)
                if prest:
                    p = prest.last()
                setattr(p,"aprobado",True)
                p.save()

                context={"respuesta":True}
                return render(request,"core/respuesta.html",context)
            else:
                context = {"respuesta":False}
                return render(request,"core/respuesta.html",context)

    context = {
        "form":form_solicitud,
        "form_id":"Solicitar",
        "title":"Solicitar Préstamo",
        "form_type": "create",
    }

    return render(request, "core/form_pedir_prestamo.html", context)

def respuesta(dni):
    url='https://api.moni.com.ar/api/v4/scoring/pre-score/'+dni
    headers = {'credential':'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
    response = requests.get(url, headers=headers)

    response_json = response.json()

    if (response_json['status']=='approve') and (response_json['has_error']==False):
        return True
    else:
        return False

