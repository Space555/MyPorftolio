from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True,
                             verbose_name='Пользователь')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='Аватар', null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    updated = models.DateTimeField(auto_now=True, verbose_name='Жата обновления')

    def __str__(self):
        return self.user.username

    def get_upload_url(self):
        return self.avatar.url

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
