from django.shortcuts import render
from django.forms import forms
from django.core.mail import send_mail

from .forms import ContactForm, TemoignageForm
from .models import Presentation, Tarif, Temoignage, Partenaires, Gallery, Service, Mention

def presentation(request):
	obj = Presentation.objects.all
	return render(request, 'main/presentation.html', {'obj':obj})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/presentation.html')
	else:
		form = ContactForm()

	return render(request, 'main/contact.html', {'form':form})

def education(request):
	obj = Service.objects.filter(page='education')
	return render(request, 'main/education.html', {'obj':obj})

def reeducation(request):
	obj = Service.objects.filter(page='reeducation')
	return render(request, 'main/reeducation.html', {'obj':obj})

def promenades(request):
	obj = Service.objects.filter(page='promenade')
	return render(request, 'main/promenades.html', {'obj':obj})

def tarifs(request):
	obj = Tarif.objects.filter(validate=True)
	return render(request, 'main/tarifs.html', {'obj':obj})

def temoignage(request):
	obj = Temoignage.objects.filter(validate=True)
	if request.method == 'POST':
		form = TemoignageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'main/presentation.html')
	else:
		form = TemoignageForm()
	return render(request, 'main/temoignage.html', {'obj':obj, 'form':form})

def gallery(request):
	obj = Gallery.objects.all()
	return render(request, 'main/gallery.html', {'obj':obj})

def partenaires(request):
	obj = Partenaires.objects.all()
	return render(request, 'main/partenaires.html', {'obj':obj})

def mention(request):
	obj = Mention.objects.all()
	return render(request, 'main/mention.html', {'obj':obj})