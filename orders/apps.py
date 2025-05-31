from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'Заказы'
    verbose_name_menu = ('Заказы') 

    def ready(self):
        # Переопределяем метаданные модели
        from .models import Order
        Order._meta.verbose_name = 'Заказ'
        Order._meta.verbose_name_plural = 'Заказы'