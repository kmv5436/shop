from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0
    verbose_name = 'Позиция заказа'
    verbose_name_plural = 'Позиции заказа'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['first_name', 'last_name', 'email', 'address']
    inlines = [OrderItemInline]

    fieldsets = (
        ('Клиент', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Адрес доставки', {
            'fields': ('address', 'postal_code', 'city')
        }),
        ('Данные заказа', {
            'fields': ('paid', 'created', 'updated')
        }),
    )
    
    readonly_fields = ['created', 'updated']