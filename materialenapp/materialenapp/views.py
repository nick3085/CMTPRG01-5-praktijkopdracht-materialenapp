from django.http import HttpResponse
from django.template.response import TemplateResponse

link = {'link': 'http://127.0.0.1:8000'}


def index(request):
    response = TemplateResponse(request, 'index.html', link)
    return response
