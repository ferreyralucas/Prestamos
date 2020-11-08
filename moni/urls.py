"""moni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import  solicitud_view, PrestamosDeleteView, Inicio, ListarPrestamos, EditarPrestamo
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view()),
    path('solicitud/',solicitud_view,name="solicitud"),
    path('prestamos/',staff_member_required(ListarPrestamos.as_view()), name='prestamos'),
    path('prestamos/<int:pk>/update',staff_member_required(EditarPrestamo.as_view())),
    path('prestamos/<int:pk>/delete',staff_member_required(PrestamosDeleteView.as_view())),
    path('accounts/', include('django.contrib.auth.urls')),
]
