from django.urls import path, include
from .views import home, welcome, pizza_menu, add_to_cart, cart_detail, update_quantity, remove_from_cart, services

urlpatterns = [
    path("home/", home, name="home"),
    path("welcome/", welcome, name="welcome"),
    path("services/", services, name="services"),
    path('menu/', pizza_menu, name='pizza_menu'),
    path('add_to_cart/<uuid:pizza_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('update-quantity/<int:item_id>/<int:quantity>/', update_quantity, name='update_quantity'),
    path('remove_from_cart/<uuid:item_id>/', remove_from_cart, name='remove_from_cart'),
    path("user/", include("user_auth.urls", namespace="user")),
]
