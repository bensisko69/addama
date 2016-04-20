from django.forms import ModelForm, Textarea
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('validate',)
        widgets = {
            'question' : Textarea(attrs={'cols': 60, 'rows': 10}),
        }

class MyCustomForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())
    content2 = MarkdownFormField()
