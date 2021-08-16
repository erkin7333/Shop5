from  django import template
from main_shop.models import Card


register = template.Library()
@register.filter()
def cart_filter(user):
    if user.is_authenticated:
        cr = Card.objects.filter(user=user).count()
        return cr

