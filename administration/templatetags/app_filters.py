from django import template

register = template.Library()

GROUP_OF_IBAN_CHARACTERS = 4


@register.filter(name='iban_format')
def iban_format(value):
    return " ".join([value[i:i+GROUP_OF_IBAN_CHARACTERS] for i in range(0, len(value), GROUP_OF_IBAN_CHARACTERS)])
