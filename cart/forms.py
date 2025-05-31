from django import forms
from django.utils.translation import gettext_lazy as _  # Импорт функции для перевода


# Русскоязычные варианты количества
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=_('Количество'),  # Русская метка для поля
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
        label=_('Перезаписать'),  # Русская метка для поля (хотя оно скрытое)
    )