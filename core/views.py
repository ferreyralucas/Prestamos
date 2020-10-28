from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolicitudForm
import requests
from .models import Prestamo
from django.views.generic.edit import DeleteView

# Create your views here.

def home_view(request):

    return render(request, "core/home.html")

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


def prestamos_list_view(request):

    queryset = Prestamo.objects.all()
    context = {
        'prestamos':queryset,
    }
    return render(request,"core/tabla_prestamos.html", context)

def prestamos_edit_view(request,pk):

    prestamo = get_object_or_404(Prestamo, id=pk)
    form = SolicitudForm(request.POST or None, instance=prestamo)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("/prestamos/")

    context = {
        'form':form,
        'form_id':'prestamo_edit',
        'Title':'Editar Solicitud',
        'form_type':'edit'
    }
    return render(request, "core/form_pedir_prestamo.html",context)

def prestamos_delete_view(request,pk):

    prestamo = get_object_or_404(Prestamo, id=pk)
    prestamo.delete()
    return redirect("/prestamos/")

class PrestamosDeleteView(DeleteView):
    model = Prestamo
    success_url = '/prestamos/'