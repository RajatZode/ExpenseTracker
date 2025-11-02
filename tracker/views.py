from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Expense
from .forms import ExpenseForm


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if not username or not email:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
        except:
            messages.error(request, "Username already exists.")
            return redirect("signup")

    return render(request, "tracker/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "tracker/login.html")


def custom_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "tracker/dashboard.html")


@login_required(login_url='login')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense added successfully!")
            return redirect('view_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})


@login_required(login_url='login')
def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by("-date")
    total = expenses.aggregate(total_amount=Sum("amount"))["total_amount"] or 0
    return render(request, "tracker/view_expenses.html", {"expenses": expenses, "total": total})


@login_required(login_url='login')
def analytics(request):
    expenses = Expense.objects.filter(user=request.user)
    category_data = expenses.values("category").annotate(total=Sum("amount"))
    return render(request, "tracker/analytics.html", {
        "category_data": category_data,
        "expenses": expenses
    })
