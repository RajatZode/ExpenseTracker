from django.shortcuts import render
from .models import Expense
from .filters import ExpenseFilter
from django.db.models import Sum

def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    expense_filter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = expense_filter.qs  # Filtered result

    # For graph data
    monthly_data = (
        expenses.values('date')
        .annotate(total=Sum('amount'))
        .order_by('date')
    )

    context = {
        'expenses': expenses,
        'expense_filter': expense_filter,
        'monthly_data': monthly_data,
    }
    return render(request, 'expenses/view_expenses.html', context)
