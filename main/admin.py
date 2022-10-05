from django.contrib import admin

from main.models import Product, Order

admin.site.register(Order)
admin.site.register(Product)
