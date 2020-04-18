from django.contrib import admin

# Register your models here.
from .models import Product, Supplier
# # Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
