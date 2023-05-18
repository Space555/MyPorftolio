from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from app_news.models import News, Category
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_news.forms import NewsForm


class NewsListView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news'


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('all_news')
    template_name = 'app_news/create_news.html'


    def form_valid(self, form):
        response =  super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return response