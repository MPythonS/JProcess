from django.contrib import admin
from .models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'order_date',
        'order_time',
        'order_total',
        'order_status',
        'order_notes',
        'j_name',
        'f_name',
        'b_name',
        'v_name',
        'package_name',
        'package_count',
        'service_name',
        'service_count'
    )
    list_filter = (
        'order_date',
        'order_time',
        'order_status',
        'j_name',
        'f_name',
        'b_name',
        'v_name',
        'package_name',
        'package_count',
        'service_name',
        'service_count'
    )
    search_fields = (
        'order_id',
        'order_date',
        'order_time',
        'order_status',
        'j_name',
        'f_name',
        'b_name',
        'v_name',
        'package_name',
        'package_count',
        'service_name',
        'service_count'
    )
    ordering = ('order_id',)
    readonly_fields = ('order_id',)
    fieldsets = (
        ('Užsakymo informacija', {
            'fields': ('order_id', 'order_date', 'order_time', 'order_total', 'order_status', 'order_notes')
        }),
        ('Sultys', {
            'fields': ('j_name', 'f_name', 'b_name', 'v_name')
        }),
        ('Pakuotės', {
            'fields': ('package_name', 'package_count')
        }),
        ('Paslaugos', {
            'fields': ('service_name', 'service_count')
        })
    )

admin.site.register(Order, OrderAdmin)