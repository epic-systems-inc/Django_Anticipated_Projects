from django.template.defaulttags import register
from django.contrib.humanize.templatetags.humanize import intcomma
from datetime import datetime

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='month_year')
def month_name(value):
    return datetime.strptime(value, '%Y-%m-%d').strftime('%b %Y')

@register.filter(name='if_none')
def no_nonesense(value):
    if value is None:
        value = 0
    return value

@register.filter(name='zero_to_blank')
def zero_to_blank(value):
    if value=="$0" or value=="0" or value==0:
        value = ''
    return value

@register.filter(name='currency')
def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s" % intcomma(int(dollars))

@register.filter(name="percentage")
def percentage(value):
    value =  str(value)
    return value+"%"