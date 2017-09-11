from django.template.response import TemplateResponse


def index(request):
    response = TemplateResponse(request, 'index.html', {'link': 'http://buurman.nickderonde.tech'})
    return response
