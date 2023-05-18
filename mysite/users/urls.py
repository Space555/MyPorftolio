from django.urls import path
from users.views import ProfileCreate, ProfileDetail, profile_update
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)

urlpatterns = [
    path('register/', ProfileCreate.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('account/<int:pk>/', ProfileDetail.as_view(), name='account'),
    path('account/update/', profile_update, name='update'),
]