from django.contrib import admin
from .models import Product, LoyalCustomer

# Register your models here.
admin.site.register(Product)
admin.site.register(LoyalCustomer)