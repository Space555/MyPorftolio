from django.urls import path
from app_news.views import NewsListView, NewsCreateView, DetailNews, UpdateNews, DeleteNews, NewsByCategoryView
from django.views.defaults import server_error, page_not_found, permission_denied


urlpatterns = [
    path('all_news/', NewsListView.as_view(), name='all_news'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
    path('all_news/<int:pk>/', DetailNews.as_view(), name='news_detail'),
    path('all_news/<int:pk>/update/', UpdateNews.as_view(), name='update_new'),
    path('all_news/<int:pk>/delete/', DeleteNews.as_view(), name='delete_new'),
    path('all_cats/<int:pk>/', NewsByCategoryView.as_view(), name='all_cats'),
]