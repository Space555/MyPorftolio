from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import ProfileForm
from users.models import Profile


class ProfileCreate(CreateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        full_name = form.cleaned_data['full_name']
        city = form.cleaned_data['city']
        avatar = form.cleaned_data['avatar']
        Profile.objects.create(user=self.object,
                               full_name=full_name,
                               city=city,
                               avatar=avatar)
        return response


