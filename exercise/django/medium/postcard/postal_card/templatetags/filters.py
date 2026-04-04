# Put you code here

from django import template

register = template.Library()

@register.filter
def persian_numbers(number):
    english_digits = '0123456789'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'

    value = str(number)

    for e,p in zip(english_digits, persian_digits):
        value = value.replace(e,p)
    return value

