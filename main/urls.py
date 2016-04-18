from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.presentation, name='presentation'),
    url(r'^tarifs', views.tarifs, name='tarifs'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^temoignage', views.temoignage, name='temoignage'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^partenaires', views.partenaires, name='partenaires'),
    url(r'^education', views.education, name='education'),
    url(r'^reeducation', views.reeducation, name='reeducation'),
    url(r'^promenades', views.promenades, name='promenades'),
    url(r'^mention', views.mention, name='mention')
    ]