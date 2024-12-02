from django.urls import path
from .views import user_login, user_register, logout_view

app_name = "user"

urlpatterns = [
    path("login/",user_login, name="login"),
    path("register/", user_register, name="register"),
    path('logout/', logout_view, name='logout'),
    
]