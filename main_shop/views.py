from django.shortcuts import render, redirect, reverse
from .models import Product, Brand, Category, Card
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AdressForm



@login_required
def product_list(request, id):
    pro = Product.objects.filter(brand_id=id)
    context = {
        "brand": pro
    }
    return render(request, 'main_shop/brand.html', context)

@login_required
def brand_list(request, id, pk):
    pro_brand = Product.objects.filter(brand_id=pk, category_id=id)
    context = {
        "categoriy_brand": pro_brand
    }
    return render(request, 'main_shop/categories.html', context)


@login_required
def cart(request):
    carts = Card.objects.filter(user=request.user)
    cart_paginator = Paginator(carts, 1)
    page_num = request.GET.get('page')
    page = cart_paginator.get_page(page_num)
    cart_total = []
    for cart in carts:
        cart_total.append(int(cart.price.split(',')[0]))
    form = AdressForm()
    context = {
        "form": form,
        'page': page,
        "carts": carts,
        "cart_total_sum": sum(cart_total),
    }
    return render(request, "main_shop/cart.html", context)

@login_required
def add_cart(request):
    if request.method == "POST":
        user = request.user
        card_category = request.POST.get('card_category')
        card_brand = request.POST.get('card_brand')
        content = request.POST.get('content')
        color = request.POST.get('color')
        price = request.POST.get('price')
        images = request.POST.get('images')
        done = Card.objects.create(user=user, card_category=card_category, card_brand=card_brand, content=content, price=price, images=images, color=color)
        if done:
            return redirect('main_shop:cart')
        return render(request, 'main_shop/cart.html')


@login_required
def cart_delete(request, pk):
    obj = Card.objects.get(pk=pk)
    obj.delete()
    return redirect('main_shop:cart')


def all_delete(request):
    obj = Card.objects.all()
    obj.delete()
    return redirect('main_shop:cart')
