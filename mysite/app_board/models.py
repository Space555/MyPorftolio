from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', null=True)
    title = models.CharField(max_length=300, verbose_name='Название объявления')
    description = models.TextField(verbose_name='Объявление')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(default=0, verbose_name='количество')
    cat_board = models.ForeignKey('CatBoard', on_delete=models.PROTECT, verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    image = models.ImageField(verbose_name='Фото')


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_board', kwargs={'pk': self.pk})
    

    def get_upload_url(self):
        return self.image
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Объявления'


class CatBoard(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self) -> str:
        return self.title