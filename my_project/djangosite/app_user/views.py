from django.shortcuts import render
from django.views.generic import TemplateView


class Account(TemplateView):
    template_name = 'app_user/user.html'
