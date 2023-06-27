from django.contrib import admin
from .models import TermModel

from django_summernote.admin import SummernoteModelAdmin


class TermAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(TermModel, TermAdmin)