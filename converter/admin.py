from django.contrib import admin
from .models import ExcelToTallyLog

@admin.register(ExcelToTallyLog)
class ExcelToTallyLogAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'converted_at', 'status')
    list_filter = ('status',)
    search_fields = ('file_name',)
