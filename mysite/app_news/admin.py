from django.contrib import admin
from app_news.models import News, Category, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'sourse_new')
    list_display_links = ('id', 'title', 'author')

admin.site.register(News, NewsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')


admin.site.register(Comment, CommentsAdmin)
