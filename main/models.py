from django.db import models
from django_markdown.models import MarkdownField
# Create your models here.

NAME_PAGE = (
    ('zephir', 'zephir'),
    ('brise', 'brise'),
    ('sirocoo', 'sirocoo'),
    ('tornade', 'tornade'),
    ('blizard', 'blizard'),
    )

class Contact(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    codePostal = models.CharField(max_length=5)
    telephone = models.CharField(max_length=10)
    question = models.TextField(max_length=300)
    validate = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    def __unicode__ (self):
        return self.nom

class Reservation(models.Model):
    text = models.TextField(max_length=900)

class Presentation(models.Model):
    text = models.TextField(max_length=900)
    file1 = models.FileField(upload_to='main/static/img/presentation')
    file2 = models.FileField(upload_to='main/static/img/presentation')

class Tarif(models.Model):
    titleText = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    titleTarif = models.CharField(max_length=100)
    tarif = models.TextField(max_length=1000)

class Partenaires(models.Model):
    file = models.ImageField(upload_to='main/static/img/partenaires')
    lien = models.CharField(max_length=250)
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom

    def __unicode__(self):
        return self.nom

class Gallery(models.Model):
    nom = models.CharField(max_length=100)
    file = models.ImageField(upload_to='media/main/img/temoignage')
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.nom

    def __unicode__(self):
        return self.nom

class Service(models.Model):
    page = models.CharField(choices=NAME_PAGE, max_length=100)
    text = models.TextField(max_length=900)
    file1 = models.FileField(upload_to='main/static/img/text')
    file2 = models.FileField(upload_to='main/static/img/text')

    def __str__(self):
        return self.page

    def __unicode__(self):
        return self.page

class MyModel(models.Model):
    content = MarkdownField()

class Mention(models.Model):
    text = models.TextField(max_length=10000)
