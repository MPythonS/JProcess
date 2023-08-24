from django.contrib import admin

from customers.models import Customer, Payment


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id',
        'customer_name',
        'customer_surname',
        'customer_phone',
        'customer_email',
        'customer_address',
        'customer_city',
        'customer_postal_code',
        'customer_notes',
    )
    list_filter = (
        'customer_name',
        'customer_surname',
        'customer_phone',
        'customer_email',
        'customer_address',
        'customer_city',
        'customer_postal_code',
        'customer_notes',
    )
    search_fields = (
        'customer_id',
        'customer_name',
        'customer_surname',
        'customer_phone',
        'customer_email',
        'customer_address',
        'customer_city',
        'customer_postal_code',
        'customer_notes',
    )
    ordering = ('customer_id',)
    readonly_fields = ('customer_id',)
    fieldsets = (
        ('Kliento informacija', {
            'fields': ('customer_id', 'customer_name', 'customer_surname', 'customer_phone', 'customer_email', 'customer_address', 'customer_city', 'customer_postal_code', 'customer_notes')
        }),
    )

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'order_id',
        'customer',
        'payment_date',
        'payment_time',
        'payment_type',
        'payment_total',
        'payment_status',
        'payment_notes',
    )
    list_filter = (
        'payment_id',
        'order_id',
        'customer',
        'payment_date',
        'payment_time',
        'payment_type',
        'payment_total',
        'payment_status',
        'payment_notes',
    )
    search_fields = (
        'payment_id',
        'order_id',
        'customer',
        'payment_date',
        'payment_time',
        'payment_type',
        'payment_total',
        'payment_status',
        'payment_notes',
    )
    ordering = ('payment_id',)
    readonly_fields = ('payment_id',)
    fieldsets = (
        ('Mokėjimo informacija', {
            'fields': ('payment_id', 'order_id', 'customer', 'payment_date', 'payment_time', 'payment_type', 'payment_total', 'payment_status', 'payment_notes')
        }),
    )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)