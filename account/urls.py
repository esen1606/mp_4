from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, UserListView, LogoutView, DashboardView, \
    activation_view, ResetPasswordView, ResetPasswordConfirmView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view()),
    path('list_users/', UserListView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('activation/', activation_view, name='activation'),
    # path('register_phone/', RegistrationPhoneView.as_view()),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('reset-password/confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
]
