from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index/index.html"


def page_404(request, exception):
    return render(request, '404.html', {})