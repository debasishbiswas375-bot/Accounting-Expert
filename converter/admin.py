from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
