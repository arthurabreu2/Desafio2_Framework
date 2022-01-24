from django.contrib import admin
from .models import JsonPlaceholder

@admin.register(JsonPlaceholder)
class JsonAdmin(admin.ModelAdmin):
    list_display = ('userId', 'id', 'title', 'completed')
    list_display_links = ('userId', 'id', 'title', 'completed')
