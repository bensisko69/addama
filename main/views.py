from django.shortcuts import render, redirect
from django.forms import forms
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import Presentation, Tarif, Partenaires, Gallery, Service, Mention

def accueil(request):
    obj = Presentation.objects.all
    return render(request, 'main/accueil.html', {'obj':obj})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                "Nouvelle demande de contact",
                "Une nouvelle demande de contact vient d'etre effectue merci d'y repondre'",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER,],
                fail_silently=False
                )
            form = ContactForm()
            return render(request, 'main/contact.html', {'form':form})
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form':form})

def reservation(request):
    return render(request, 'main/reservation.html')

def zephir(request):
    obj = Service.objects.filter(page='zephir')
    return render(request, 'main/zephir.html', {'obj':obj})

def sirocoo(request):
    obj = Service.objects.filter(page='sirocoo')
    return render(request, 'main/sirocoo.html', {'obj':obj})

def tornade(request):
    obj = Service.objects.filter(page='tornade')
    return render(request, 'main/tornade.html', {'obj':obj})

def blizard(request):
    obj = Service.objects.filter(page='blizard')
    return render(request, 'main/blizard.html', {'obj':obj})

def brise(request):
    obj = Service.objects.filter(page='brise')
    return render(request, 'main/brise.html', {'obj':obj})

def tarifs(request):
    obj = Tarif.objects.filter(validate=True)
    return render(request, 'main/tarifs.html', {'obj':obj})

def gallery(request):
    obj = Gallery.objects.all()
    return render(request, 'main/gallery.html', {'obj':obj})

def partenaires(request):
    obj = Partenaires.objects.all()
    return render(request, 'main/partenaires.html', {'obj':obj})

def mention(request):
    obj = Mention.objects.all()
    return render(request, 'main/mention.html', {'obj':obj})
