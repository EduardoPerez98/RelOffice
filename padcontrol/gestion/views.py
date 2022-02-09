import xml.etree.ElementTree as ET

from xml.dom import minidom
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from gestion.forms import Oficioform, Depeform, Anaform
from gestion.models import Oficios, Dependencias, Analistas


def detalle_Oficio(request, id):
    oficio = get_object_or_404(Oficios, pk=id)
    # oficio = Oficios.objects.all()
    # dependencia = Dependencias.objects.all()
    return render(request, 'oficios/detalle_oficio.html', {'oficio': oficio})


def Nuevo_Oficio(request):
    if request.method == 'POST':
        formaOficio = Oficioform(request.POST)
        if formaOficio.is_valid():
            formaOficio.save()
            return redirect('index')
    else:
        formaOficio = Oficioform()

    return render(request, 'oficios/nuevo_oficio.html', {'formaOficio': formaOficio})


def Editar_Oficio(request, id):
    oficio = get_object_or_404(Oficios, pk=id)
    if request.method == 'POST':
        formaOficio = Oficioform(request.POST, instance=oficio)
        if formaOficio.is_valid():
            formaOficio.save()
            return redirect('index')
    else:
        formaOficio = Oficioform(instance=oficio)

    return render(request, 'oficios/editar_oficio.html', {'formaOficio': formaOficio})


#############

def Nueva_Depe(request):
    if request.method == 'POST':
        formaDepe = Depeform(request.POST)
        if formaDepe.is_valid():
            formaDepe.save()
        return redirect('asignados')
    else:
        formaDepe = Depeform()

    return render(request, 'dependencias/nueva_depe.html', {'formaDepe': formaDepe})


def Editar_Depe(request, clave):
    depe = get_object_or_404(Dependencias, pk=clave)
    if request.method == 'POST':
        formaDepe = Depeform(request.POST, instance=depe)
        if formaDepe.is_valid():
            formaDepe.save()
            return redirect('asignados')
    else:
        formaDepe = Depeform(instance=depe)

    return render(request, 'dependencias/editar_depe.html', {'formaDepe': formaDepe})

###########

def Editar_Analista(request,id):
    analista = get_object_or_404(Analistas, pk=id)
    if request.method == 'POST':
        formaAna = Anaform(request.POST, instance=analista)
        if formaAna.is_valid():
            formaAna.save()
            return redirect ('analistas')
    else:
        formaAna = Anaform(instance=analista)

    return render(request, 'analistas/editar_analista.html',{'formaAna':formaAna})

