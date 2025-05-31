from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=_('Количество'),
        widget=forms.Select(attrs={
            'class': 'form-control quantity-select',
            'style': 'width: 80px; display: inline-block;'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        initial_quantity = kwargs.pop('initial_quantity', 1)
        super().__init__(*args, **kwargs)
        self.fields['quantity'].initial = initial_quantity