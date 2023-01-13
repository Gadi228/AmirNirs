from django import template
from sport.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return View.objects.all()
    else:
        return View.objects.filter(pk=filter)

@register.inclusion_tag('sport/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = View.objects.all()
    else:
        cats = View.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
