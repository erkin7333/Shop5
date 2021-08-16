from  django import template
from main_shop.models import Brand


register = template.Library()

@register.simple_tag()
def get_brands():
    return Brand.objects.all()



