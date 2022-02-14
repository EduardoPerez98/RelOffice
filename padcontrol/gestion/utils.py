from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def generador_pdf(template_src, context_dict={}):
    # Se obtiene el HTML sin contexto
    template = get_template(template_src)
    # Aquí se incluye el contexto de Django
    html = template.render(context_dict)
    result = BytesIO
    # Aquí se hace la transformacion a PDF de ambos recursos solicitados
    # Otra obtencion de bits que transforman el pdf
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpRequest(result.getvalue(), content_type='application/pdf')
    
    return None
