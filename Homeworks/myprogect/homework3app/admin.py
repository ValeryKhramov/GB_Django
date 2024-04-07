from django.contrib import admin
from .models import Product, Order, Client


@admin.action(description="Сбросить количество товара")
def reset_count_products(modeladmin, request, queryset):
    queryset.update(count_products=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count_products']
    search_fields = ['name']
    search_help_text = 'Поиск по наименованию продукта'
    readonly_fields = ['date_added']
    actions = [reset_count_products]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'count_products'],
            }
        ),
        (
            'Подробности о товаре',
            {
                'classes': ['collapse'],
                'description': 'Дополнительная информация о товаре',
                'fields': ['description', 'image'],
            }
        ),
        (
            'Дата добавления товара',
            {
                'fields': ['date_added']
            }
        )
    ]


class OrderAdmin(admin.ModelAdmin):
    search_help_text = 'Поиск по клиенту'
    readonly_fields = ['date_of_registration']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number_phone']
    search_fields = ['name']
    search_help_text = 'Поиск клиента по имени'
    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'number_phone'],
            }
        ),
        (
            'Подробности о клиенте',
            {
                'classes': ['collapse'],
                'description': 'Дополнительная информация о клиенте',
                'fields': ['email', 'address'],
            }
        ),
        (
            'Дата регистрации',
            {
                'fields': ['registration_date'],
            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
