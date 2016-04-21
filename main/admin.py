from django.contrib import admin
from django.db import models
from django_markdown.admin import MarkdownModelAdmin

from .models import Contact, Presentation, Tarif, Partenaires, Gallery, Service, MyModel, Mention, Reservation, Rejoindre

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('nom', 'telephone')
    list_filter = ['validate']

class PresentationAdmin(admin.ModelAdmin):
    model = Presentation

class TarifAdmin(admin.ModelAdmin):
    model = Tarif
    fieldsets = (
        ('Tarif', {'fields':('titleTarif', 'tarif')}),
        ('Text', {'fields':('titleText', 'text')})
        )

class PartenairesfAdmin(admin.ModelAdmin):
    model = Partenaires

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery

class ServiceAdmin(admin.ModelAdmin):
    model = Service

class MentionAdmin(admin.ModelAdmin):
    model = Mention

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation

class RejoindreAdmin(admin.ModelAdmin):
    model = Rejoindre

admin.site.register(Contact, ContactAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Partenaires, PartenairesfAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(MyModel, MarkdownModelAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Rejoindre, RejoindreAdmin)