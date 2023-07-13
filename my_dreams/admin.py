from django.contrib import admin

from my_dreams.models import Dream


@admin.register(Dream)
class DreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'wish_rate', 'time_to_complete')