from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'full_name',
            'gender',
            'national_code',
            'birthday_date',
            'ceremony_datetime',
            'country',
        ]

    def clean_national_code(self):
        nc = self.cleaned_data.get('national_code', '')
        if len(nc) != 10:
            raise ValidationError('national_code must contain exactly 10 characters.')
        return nc

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name', '').strip()
        parts = full_name.split(' ')
        # Must contain exactly first and last name
        if len(parts) != 2:
            raise ValidationError('full_name must include exactly first_name and last_name separated by a single space.')
        # Both parts must be title-cased (start with uppercase, rest lowercase)
        if not all(p.istitle() for p in parts):
            raise ValidationError('Both first and last names must be title-cased (e.g. "Arash Ghasemi").')
        return full_name
