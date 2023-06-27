from django import forms
from .models import TechModel

from django_summernote.widgets import SummernoteWidget


class TechForm(forms.ModelForm):

    class Meta:
        model = TechModel
        fields = ('title', 'text', 'thumbnail')
        widgets = {
                'text': SummernoteWidget(),
        }