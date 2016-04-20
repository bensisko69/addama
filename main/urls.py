from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^tarifs', views.tarifs, name='tarifs'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^partenaires', views.partenaires, name='partenaires'),
    url(r'^zephir', views.zephir, name='zephir'),
    url(r'^sirocoo', views.sirocoo, name='sirocoo'),
    url(r'^brise', views.brise, name='brise'),
    url(r'^tornade', views.tornade, name='tornade'),
    url(r'^blizard', views.blizard, name='blizard'),
    url(r'^mention', views.mention, name='mention')
    ]
