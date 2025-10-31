from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Home redirect to login
def home(request):
    return redirect('login')

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Signup successful! Please login.")
        return redirect('login')

    return render(request, 'tracker/signup.html')


# Login View
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'tracker/login.html')


# Logout View
def logout_user(request):
    auth.logout(request)
    return redirect('login')


# Forgot Password View
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.success(request, "Password reset link sent to your email.")
        else:
            messages.error(request, "Email not found.")
        return redirect('forgot_password')
    return render(request, 'tracker/forgot_password.html')


# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'tracker/dashboard.html')
