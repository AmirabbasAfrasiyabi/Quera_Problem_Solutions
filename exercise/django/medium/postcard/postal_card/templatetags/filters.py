from django import template

register = template.Library()

@register.filter

def persian_digits(value):
    if value is None:
        return ''

    english_digits = '0123456789'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'

    translation_table = str.maketrans(english_digits, persian_digits)

    return str(value).translate(translation_table)