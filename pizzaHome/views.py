from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pizza, Cart, CartItems

def welcome(request):
    return render(request, "welcome.html")

@login_required(login_url='user:login')
def home(request):
    pizzas = Pizza.objects.all()
    return render(request, "home.html")


def services(request):
    return render(request, "services.html")


def pizza_menu(request):
    pizzas = Pizza.objects.select_related('category').all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizza_menu.html', context)



# @login_required
def add_to_cart(request, pizza_id):  
    pizza = Pizza.objects.get(uid=pizza_id)
    cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)

    cart_item, created = CartItems.objects.get_or_create(
        cart=cart, pizza=pizza,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

# @login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    cart_items = cart.cart_items.all() if cart else []
    

    for item in cart_items:
        item.total_price = item.pizza.price * item.quantity
    
    subtotal = sum(item.total_price for item in cart_items)
    delivery_fee = 0.90  
    total_price = subtotal + delivery_fee

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

# @login_required
def update_quantity(request, item_id, quantity):
    cart_item = get_object_or_404(CartItems, id=item_id, cart__user=request.user, cart__is_paid=False)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart_detail')

# @login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItems, id=item_id, cart__user=request.user, cart__is_paid=False)
    cart_item.delete()
    return redirect('cart_detail')