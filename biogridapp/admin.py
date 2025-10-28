from django.contrib import admin
from .models import Biography

# Register your models here.
@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('name','occupation','nationality','created_at')
    search_fields = ('name','occupation','nationality')