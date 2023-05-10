from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class Index(TemplateView):
    template_name = 'app_index/index.html'
