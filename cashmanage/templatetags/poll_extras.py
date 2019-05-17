from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value):
    ret_arr = []
    for item in value:
        item.replace('&#38', 'aa')
        ret_arr.append(item)
    return ret_arr


