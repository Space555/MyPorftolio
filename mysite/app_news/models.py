from django.db import models
from django.contrib.auth.models import User
from datetime import timezone, datetime, date
from django.urls import reverse



class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    title = models.CharField(max_length=300, verbose_name='Название')
    descr = models.TextField(verbose_name='Новость')
    link_new = models.CharField(verbose_name='Ссылка на источник', max_length=500)
    sourse_new = models.CharField(max_length=300, verbose_name='Источник новости')
    created = models.DateTimeField(default=datetime.now(), verbose_name='Дата создания')
    updated = models.DateTimeField(default=datetime.now(), verbose_name='Дата обновления')
    category_new = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField(upload_to='img_news/%Y/%m/%d/', verbose_name='Фото новостей', null=True, blank=True)

    def __str__(self):
        return self.author.username

    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
    
    def get_upload_url(self):
        return self.image.url
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категории', null=True, blank=True)


    def __str__(self):
        return self.title  
     
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='usercomemnt',
                             null=True, blank=True)
    text = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Пост комментария', related_name='news')
    created = models.DateField(auto_now_add=True, verbose_name='создан')
    updated = models.DateField(auto_now=True, verbose_name='обновлен')
    count_comments = models.IntegerField(verbose_name='Счетчик комментариев', default=0)

    def __str__(self):
        return self.news.title

    def comments_count(self):
        return self.count_comments

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
