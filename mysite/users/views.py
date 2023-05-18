from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView
from users.forms import ProfileForm, UserUpdateForm, ProfileUpdateForm
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


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/account.html'
    context_object_name = 'account'


@login_required
def profile_update(request):
    """Представление смены информации о пользователе"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account', pk=request.user.pk)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update_profile.html', context)