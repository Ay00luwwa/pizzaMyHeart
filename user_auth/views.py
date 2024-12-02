from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def user_login(request):
    return render(request, "login.html")

@login_required
def home(request):
    return redirect (request, "home.html")

def user_register(request):
    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect('user:login')