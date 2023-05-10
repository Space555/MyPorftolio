from django.urls import path
from app_user.views import Account

urlpatterns = [
    path('account/', Account.as_view(), name='account')
]