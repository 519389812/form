from django.contrib import admin
from .models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'greeting', 'eye_contact', 'smile', 'message', 'time', 'ip_address']
    list_filter = ('greeting', 'eye_contact', 'smile', 'message', 'time',)  # 过滤器
    search_fields = ('staff',)  # 搜索字段
    date_hierarchy = 'time'  # 详细时间分层筛选　


admin.site.site_header = '服务评价管理系统'
admin.site.site_title = '服务评价管理系统'
admin.site.register(Rate, RateAdmin)
