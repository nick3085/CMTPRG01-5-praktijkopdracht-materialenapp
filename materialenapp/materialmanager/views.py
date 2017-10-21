from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from xhtml2pdf import pisa
from .models import Delivery


# Generic Index deliveries
class IndexView(ListView):
    template_name = 'materialmanager/index.html'
    context_object_name = 'all_deliveries'

    def get_queryset(self):
        return Delivery.objects.all()


# Generic Detail delivery
class DetailDeliveryView(DetailView):
    model = Delivery
    template_name = 'materialmanager/detail.html'


# Generic Create Detail delivery
class DeliveryCreate(CreateView):
    model = Delivery
    fields = ['supplier', 'location', 'photo', 'processing', 'categories', 'weight', 'note', 'active']


# Generic Update Detail delivery
class DeliveryUpdate(UpdateView):
    model = Delivery
    fields = ['supplier', 'location', 'photo', 'processing', 'categories', 'weight', 'note', 'active']


# Generic delete Detail delivery
class DeliveryDelete(DeleteView):
    model = Delivery
    success_url = reverse_lazy('materialmanager:index')


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



