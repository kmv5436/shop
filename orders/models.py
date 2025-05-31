from django.db import models
from shop.models import Product

class Order(models.Model):
    first_name = models.CharField(('Имя'), max_length=50)
    last_name = models.CharField(('Фамилия'), max_length=50)
    email = models.EmailField()
    address = models.CharField(('Адрес'), max_length=250)
    postal_code = models.CharField(('Почтовый индекс'), max_length=20)
    city = models.CharField(('Город'), max_length=100)
    created = models.DateTimeField(('Создать'), auto_now_add=True)
    updated = models.DateTimeField(('Обновить'), auto_now=True)
    paid = models.BooleanField(('Оплаченный'), default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Заказы {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    price = models.DecimalField('Цена', max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity