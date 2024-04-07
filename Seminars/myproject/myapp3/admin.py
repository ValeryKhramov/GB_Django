from django.contrib import admin
from .models import Coin, Cub, Numbers, Author, Post


@admin.action(description='Тестовая активность')
def admin_test(modeladmin, request, queryset):
    queryset.update(name='text_test')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'second_name', 'email']
    ordering = ['name']
    list_filter = ['second_name']
    search_fields = ['name']
    # fields = ['name', 'second_name', 'email', 'biography', 'birthday']
    readonly_fields = ['birthday']
    actions = [admin_test]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'second_name'],
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Дополнительные данные об авторе',
                'fields': ['email', 'biography', 'birthday'],
            }
        ),
    ]


admin.site.register(Coin)
admin.site.register(Cub)
admin.site.register(Numbers)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
