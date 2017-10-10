from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# namespacing so the app knows where to look when there are more apps with de same name='detail'
app_name = 'materialmanager'

urlpatterns = [
    # /materialmanager/
    url(r'^$', views.index, name='index'),

    # /materialmanager/delivery_id/
    url(r'^(?P<delivery_id>[0-9]+)/$', views.detail, name='detail'),

    # /materialmanager/delivery_id/active
    url(r'^(?P<delivery_id>[0-9]+)/$', views.detail, name='active'),


    # /materialmanager/pdf/
    url(r'^pdf$', views.get_pdf, name='delivery_pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
