from django import template

register = template.Library()

@register.filter
def determine_word(x):
    if x % 10 in [2, 3, 4] and x % 100 not in [12, 13, 14]:
        return "раза"
    else:
        return "раз"