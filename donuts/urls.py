from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<donut_id>[0-9]+)/$', views.detail, name='detail'),
]
