from django.contrib import admin
from app_board.models import Board, CatBoard

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Board, BoardAdmin)


class CatBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(CatBoard, CatBoardAdmin)