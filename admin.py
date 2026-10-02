from django.contrib import admin
from .models import MeterReading, Profile

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slno', 'quarterno', 'meterreading', 'created_at')
    search_fields = ('user__username', 'slno', 'quarterno')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Profile)
