from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@csrf_protect
def user_login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')  # Ensure the input name in your form is 'email'
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)  # Use `username=email` since the backend expects this
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace with the name of your home URL pattern
        else:
            context['error'] = 'Invalid email or password'

    return render(request, "login.html", context)


@csrf_protect
def user_register(request):
    if request.method == 'POST':
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('user:login')  # Redirect to the login page after successful registration

    return render(request, "register.html")


@login_required
def home(request):
    return redirect (request, "home.html")

def logout_view(request):
    logout(request)
    return redirect('user:login')