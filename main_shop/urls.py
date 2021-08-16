from django.urls import path
from . import views


app_name = "main_shop"

urlpatterns = [
    path('categoriya/<int:id>/', views.product_list, name='categoriya'),
    path('category_brand/<int:pk>/<int:id>/', views.brand_list, name='category_brand'),
    path('cart/', views.cart, name="cart"),
    path('add/cart/', views.add_cart, name='add-cart'),
    path('delete/<int:pk>/', views.cart_delete, name='delete'),
    path('all_delete/', views.all_delete, name='all-delete'),
    # path('cat/<int:pk>/', views.Pagi.as_view(), name='cat')
]

