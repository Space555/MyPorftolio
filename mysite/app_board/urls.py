from django.urls import path
from app_board.views import AnnouncementListView

urlpatterns = [
    path('announcement/', AnnouncementListView.as_view(), name='all_board'),
]