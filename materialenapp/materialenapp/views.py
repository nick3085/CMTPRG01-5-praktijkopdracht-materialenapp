from django.template.response import TemplateResponse


def index(request):
    response = TemplateResponse(request, 'index.html', {'link': 'http://127.0.0.1'})
    return response
