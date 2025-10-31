from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def home(request):
    return render(request, 'tracker/home.html')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_expense')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

def view_expense(request):
    expenses = Expense.objects.all()
    return render(request, 'tracker/view_expense.html', {'expenses': expenses})
