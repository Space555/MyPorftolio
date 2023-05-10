from django.urls import path
from app_index.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]