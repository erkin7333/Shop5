from django.contrib import admin
from . models import *




admin.site.register(Product)
admin.site.register(Smartphone)
admin.site.register(Televizor)
admin.site.register(Notebook)
admin.site.register(Category)
admin.site.register(Muzlatkich)
admin.site.register(Konditsaner)
admin.site.register(Gaz)

# class AdminProduct(admin.ModelAdmin):
#     class Meta:
#         model = Product
# admin.site.register(Product, AdminProduct)