from django.urls import path
from .views import CustomLoginView
from . import views
from django.contrib.auth.views import LogoutView
from users.forms import EmailAuthenticationForm
from django.contrib.auth.views import LoginView  # Import LoginView
from .views import CustomLoginView



app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # Use your custom view
    path('login/', LoginView.as_view(authentication_form=EmailAuthenticationForm), name='login'),
    path('register/', views.account_register, name='register'),  # Register page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('vote/<int:session_id>/', views.vote, name='vote'),  # Voting page
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('voter_dashboard/', views.voter_dashboard, name='voter_dashboard'),
    path('results/<int:session_id>/', views.voting_results, name='voting_results'),
]
