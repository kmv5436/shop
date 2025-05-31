from django.contrib import admin
from .models import Category, Product
admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Управление сайтом'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
    # Русские названия для полей в админке
    list_display_labels = {
        'name': 'Название',
        'slug': 'Слаг',
        'price': 'Цена',
        'available': 'Доступен',
        'created': 'Создан',
        'updated': 'Обновлен',
    }
    
    # Русские названия для фильтров
    list_filter_labels = {
        'available': 'Доступность',
        'created': 'Дата создания',
        'updated': 'Дата обновления',
    }
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'