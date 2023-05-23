from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app_news.models import News, Category, Comment
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_news.forms import NewsForm, CommentForm
from django.shortcuts import redirect


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
    

class DetailNews(DetailView):
    model = News
    template_name = 'app_news/detail_news.html'
    context_object_name = 'info_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.prefetch_related('user').filter(
            news=self.get_object()).order_by('-created')
        context['form'] = CommentForm()
        return context

    def post(self, request, **kwargs):
        news_detail = self.get_object()
        comments_form = CommentForm(request.POST)
        if comments_form.is_valid():
            Comment.objects.create(news=news_detail, user=self.request.user, **comments_form.cleaned_data)
            return redirect('news_detail', pk=news_detail.pk)


class UpdateNews(UpdateView):
    model = News
    template_name = 'app_news/update_news.html'
    form_class = NewsForm
    
    def get_success_url(self):
        return reverse_lazy('news_detail',  kwargs={'pk': self.object.pk})
    

class DeleteNews(DeleteView):
    model = News
    template_name = 'app_news/delete.html'
    success_url = reverse_lazy('all_news')



class NewsByCategoryView(ListView):
    """Представление для отображения новостей по категориям"""
    template_name = 'app_news/category.html'
    model = News
    context_object_name = 'cats'

    def get_queryset(self):
        print(News.objects.filter(category_new_id=self.kwargs['pk']))
        return News.objects.filter(category_new_id=self.kwargs['pk'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = Category.objects.get(id=self.kwargs['pk'])
    #     return context
