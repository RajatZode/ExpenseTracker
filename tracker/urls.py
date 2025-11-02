from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # Expense Pages
    path('add/', views.add_expense, name='add_expense'),
    path('view/', views.view_expenses, name='view_expenses'),
    path('analytics/', views.analytics, name='analytics'),

    # Forgot Password URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='tracker/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='tracker/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tracker/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tracker/password_reset_complete.html'), name='password_reset_complete'),
]
