from django.contrib import admin
from .models import TopicModel

from django_summernote.admin import SummernoteModelAdmin


class TopicAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(TopicModel, TopicAdmin)