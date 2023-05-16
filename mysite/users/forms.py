from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(UserCreationForm):
    full_name = forms.CharField(required=True, label='', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО *',
                                                                                        'class': 'register-input'}))
    avatar = forms.ImageField(label='', required=False)
    city = forms.CharField(required=True, label='', max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Введите город *', 'class': 'register-input'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя *',
                                                                       'class': 'register-input'}))
    email = forms.CharField(required=True, label='', widget=forms.EmailInput(attrs={'placeholder': 'Введите Email *',
                                                                     'class': 'register-input'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль *',
                                                                            'class': 'register-input'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль *',
                                                                            'class': 'register-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
