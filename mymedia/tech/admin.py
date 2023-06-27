from django.contrib import admin
from .models import TechModel

from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(TechModel, BlogAdmin)