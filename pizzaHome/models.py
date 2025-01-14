from django.db import models
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
    
class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
    
    
    
    

class Pizza(BaseModel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to="pizza")
    
    def __str__(self):
        return self.pizza_name
    
    
    
    
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="carts")
    is_paid = models.BooleanField(default=False)
    
    
    
    
    
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.pizza} in Cart #{self.cart.uid}"
    
     
     
    # def __str__(self):
    #     return f"{self.pizza} in Cart #{self.cart.uid}"