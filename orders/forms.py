from django.utils.safestring import mark_safe
from django import forms
from django.core.validators import ValidationError
from .models import Order


class OrderCreateForm(forms.ModelForm):
    privacy_policy = forms.BooleanField(
        label='Я согласен с <a href="/privacy/">Политикой конфиденциальности</a>',
        required=True,
        error_messages={
            'required': 'Вы должны принять Политику конфиденциальности для оформления заказа'
        }
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                 'postal_code', 'city', 'privacy_policy']
        widgets = {
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Делаем все поля обязательными
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Особые настройки для поля privacy_policy
        self.fields['privacy_policy'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['privacy_policy'].label = mark_safe(
            'Я согласен с <a href="/privacy/" target="_blank">Политикой конфиденциальности</a>'
        )

    def clean_privacy_policy(self):
        accepted = self.cleaned_data.get('privacy_policy')
        if not accepted:
            raise ValidationError("Необходимо ваше согласие с Политикой конфиденциальности")
        return accepted