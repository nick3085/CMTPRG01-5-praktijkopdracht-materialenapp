from django.template import Context
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.datetime_safe import datetime

from xhtml2pdf import pisa

from .models import Delivery


def index(request):
    return HttpResponse("Index page of the materialmanager")


def get_pdf(request):
    data = Delivery.objects.all()
    template = get_template('pdf/deliveries.html')
    html = template.render({
        "deliveries": data,
        "time": datetime.now(),
    })
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf', )
    return HttpResponse('We had some errors<pre>%s</pre>')
