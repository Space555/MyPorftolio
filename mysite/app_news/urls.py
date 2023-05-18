from django.urls import path
from app_news.views import NewsListView, NewsCreateView


urlpatterns = [
    path('all_news/', NewsListView.as_view(), name='all_news'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
]