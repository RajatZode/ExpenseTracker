import django_filters
from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte', label='From Date')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte', label='To Date')
    category = django_filters.CharFilter(lookup_expr='icontains', label='Category')

    class Meta:
        model = Expense
        fields = ['category', 'start_date', 'end_date']