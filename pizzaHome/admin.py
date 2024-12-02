from django.contrib import admin

from .models import PizzaCategory, Pizza, Cart, CartItems

admin.site.register(PizzaCategory)
admin.site.register(Pizza)
admin.site.register(Cart)
admin.site.register(CartItems)