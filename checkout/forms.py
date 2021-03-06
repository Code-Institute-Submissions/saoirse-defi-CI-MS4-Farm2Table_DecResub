from crispy_forms.helper import FormHelper

from django import forms
from .models import Order


class TestForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email',
                  'phone_number', 'street_address1',
                  'street_address2', 'town',
                  'county', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        """Adds placeholders and classes,
            remove auto-gen labels and sets
            autofocus on first field."""

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone',
            'street_address1': 'Street Address Line 1',
            'street_address2': 'Street Address Line 2',
            'town': 'Town/City',
            'county': 'County',
            'postcode': 'Eircode',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
