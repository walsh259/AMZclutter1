from django.contrib import admin

# Register your models here.
from .models import Product, Supplier, Designer, Trademark, Shipmark
# # Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Designer)
admin.site.register(Trademark)
admin.site.register(Shipmark)
