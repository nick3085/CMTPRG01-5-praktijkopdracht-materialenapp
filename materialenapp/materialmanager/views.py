from io import BytesIO
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime

from xhtml2pdf import pisa
from .models import Delivery


# Index model for the deliveries in materialmanager
def index(request):
    all_deliveries = Delivery.objects.all()
    context = {'all_deliveries': all_deliveries,}
    return render(request, 'materialmanager/index.html', context)


# Detail model for delivery in materialmanager
def detail(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    context = {'delivery': delivery}
    return render(request, 'materialmanager/detail.html', context)


# function for the pdf generator request
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



