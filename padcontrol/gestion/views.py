import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse

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

def Editar_Analista(request, id):
    analista = get_object_or_404(Analistas, pk=id)
    if request.method == 'POST':
        formaAna = Anaform(request.POST, instance=analista)
        if formaAna.is_valid():
            formaAna.save()
            return redirect('analistas')
    else:
        formaAna = Anaform(instance=analista)

    return render(request, 'analistas/editar_analista.html', {'formaAna': formaAna})


#####
def report(request):
    response = HttpResponse(content_type='applicaction/pdf')
    response['Content-Disposition'] = 'attachment: filename=Contrato-ingreso-asignatura.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # ENCABEZADO DEL PDF
    c.setLineWidth(.3)
    c.setFont('Arial Narrow', 22)
    c.drawString(30, 750, 'CONTRATO POR TIEMPO DETERMINADO')

    c.setFont('Arial Narrow-Bold', 12)
    c.drawString(30, 735, 'UNIVERSIDAD AUTONOMA DE CHIAPAS')

    c.setFont('Arial Narrow-Bold', 12)
    c.drawString(480, 750, "11/02/2022")
    c.line(460, 747, 560, 747)

    styles = getSampleStyleSheet()
    styleBH = styles["normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 14

    numero = Paragraph('''No.''', styleBH)
    nombrema = Paragraph('''Asignatura''', styleBH)
    grupoma = Paragraph('''Grupo''', styleBH)
    HSM = Paragraph('''H/S/M''', styleBH)
    total = Paragraph('''Total''', styleBH)

    data = []
    data.append([numero, nombrema, grupoma, HSM, total])

    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 8

    high = 650
    for asignatura in asignaturas:
        this_asignatura = [asignatura['numero'], asignatura['nombrema'], asignatura['grupoma'], asignatura['HSM'],
                           asignatura['total']]
        data.append(this_asignatura)
        high = high - 18

    width, heigth = A4
    table = Table(data, colWidths=[1.9 * cm, 9.5 * cm, 1.9 * cm, 1.9 * cm, 1.9 * cm])
    table.setStyle(TableStyle([  # ESTILOS DE LA TABLA
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
