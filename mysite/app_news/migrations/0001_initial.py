# Generated by Django 4.2.1 on 2023-05-18 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('descr', models.TextField(verbose_name='Новость')),
                ('link_new', models.TextField(verbose_name='Ссылка на источник')),
                ('sourse_new', models.CharField(max_length=300, verbose_name='Источник новости')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category_new', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_news.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_news.news', verbose_name='Новость'),
        ),
    ]
