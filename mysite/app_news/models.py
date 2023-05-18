from django.db import models
from django.contrib.auth.models import User
from datetime import timezone, datetime
from django.urls import reverse



class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    title = models.CharField(max_length=300, verbose_name='Название')
    descr = models.TextField(verbose_name='Новость')
    link_new = models.CharField(verbose_name='Ссылка на источник', max_length=500)
    sourse_new = models.CharField(max_length=300, verbose_name='Источник новости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category_new = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.author.username

    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
    
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