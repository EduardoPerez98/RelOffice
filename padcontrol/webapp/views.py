from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from gestion.models import Oficios, Dependencias, Analistas


def index(request):
    oficios = Oficios.objects.order_by('-fecha')
    no_oficios = Oficios.objects.count()
    return render(request, 'inicio.html', {'Oficios': oficios, 'no_oficios': no_oficios})


def asignados(request):
    dependencias = Dependencias.objects.order_by('clave')
    no_depen = Dependencias.objects.count()
    return render(request, 'asignados.html',
                  {'Dependencias': dependencias, 'no_depen': no_depen})


def Analistas_asignados(request):
    analistas = Analistas.objects.order_by('id')
    no_analistas = Analistas.objects.count()
    return render(request, 'analistas.html', {'Analistas': analistas, 'no_analistas': no_analistas})

def Historial_ofi(request):
    oficios = Oficios.objects.order_by('-fecha')
    no_oficios = Oficios.objects.count()
    return render(request, 'historialofi.html',{'Oficios':oficios, 'no_oficios':no_oficios})