from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pdf$', views.get_pdf, name='delivery_pdf'),
]
