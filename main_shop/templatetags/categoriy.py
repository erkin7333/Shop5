from  django import template
from main_shop.models import Category


register = template.Library()

@register.simple_tag()
def get_categoriy():
    return Category.objects.all()
