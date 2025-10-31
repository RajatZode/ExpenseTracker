from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth routes
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Expenses page
    path('expenses/', views.view_expenses, name='view_expenses'),
]
