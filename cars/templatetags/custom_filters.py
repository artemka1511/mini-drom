from django import template

register = template.Library()


@register.filter(name='beautiful_price')
def beautiful_price(value):
    if len(str(value)) == 5:
        value = str(value)[:2] + ' ' + str(value)[2:5] + ' ₽'
    elif len(str(value)) == 6:
        value = str(value)[:3] + ' ' + str(value)[3:6] + ' ₽'
    elif len(str(value)) == 7:
        value = str(value)[:1] + ' ' + str(value)[1:4] + ' ' + str(value)[4:7] + ' ₽'
    elif len(str(value)) == 8:
        value = str(value)[:2] + ' ' + str(value)[2:5] + ' ' + str(value)[5:8] + ' ₽'
    return value
