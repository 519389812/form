from django.contrib import admin
from .models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'star', 'time', 'ip_address']


admin.site.register(Rate, RateAdmin)
