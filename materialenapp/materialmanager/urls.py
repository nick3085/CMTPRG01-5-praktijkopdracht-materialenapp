from django.conf.urls import url
from . import views

# namespacing so the app knows where to look when there are more apps with de same name='detail'
app_name = 'materialmanager'

urlpatterns = [
    # index view /materialmanager/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # detail delivery view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailDeliveryView.as_view(), name='detail'),

    # add delivery view
    url(r'^delivery/add/$', views.DeliveryCreate.as_view(), name='delivery-add'),

    # update delivery view
    url(r'^delivery/(?P<pk>[0-9]+)/$', views.DeliveryUpdate.as_view(), name='delivery-update'),

    # delete delivery view
    url(r'^delivery/(?P<pk>[0-9]+)/delete/$', views.DeliveryDelete.as_view(), name='delivery-delete'),

    # /materialmanager/pdf/
    url(r'^pdf/$', views.get_pdf, name='delivery-pdf'),
]