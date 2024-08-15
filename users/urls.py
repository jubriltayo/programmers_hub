from django.urls import path
from .views import PingView, RegisterView, LoginView, UserDetailView


urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'), # for cron job only
    
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('user/<int:userId>/', UserDetailView.as_view(), name='user-detail'),
]
