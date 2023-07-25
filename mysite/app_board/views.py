from django.shortcuts import render
from django.views.generic import ListView
from app_board.models import Board


class AnnouncementListView(ListView):
    model = Board
    template_name = 'app_board/board_list.html'
    context_object_name = 'boards'