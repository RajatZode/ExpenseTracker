from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('add/', views.add_expense, name='add_expense'),
    path('view/', views.view_expenses, name='view_expenses'),
    path('analytics/', views.analytics, name='analytics'),
]
