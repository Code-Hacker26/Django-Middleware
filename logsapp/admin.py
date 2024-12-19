from django.contrib import admin
from .models import RequestLog,LogEntry

admin.site.register(RequestLog)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'method', 'status_code', 'timestamp')
    list_filter = ('status_code', 'method')
    search_fields = ('path',)
    ordering = ('-timestamp',)