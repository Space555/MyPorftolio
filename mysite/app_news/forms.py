from django import forms
from app_news.models import News, Category


class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=300, label='Заголовок', widget=forms.TextInput(attrs={'class': 'create__form-input'}))
    descr = forms.CharField(label='Новость', widget=forms.Textarea(attrs={'class': 'create__form-textarea'}))
    link_new = forms.CharField(label='Ссылка на новость', widget=forms.TextInput(attrs={'class': 'create__form-input'}), max_length=500)
    sourse_new = forms.CharField(label='Источник новости', widget=forms.TextInput(attrs={'class': 'create__form-input'}), max_length=500)
    category_new = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберете категорию', label='Категория')
    class Meta:
        model = News
        fields = ('title', 'descr', 'link_new', 'sourse_new', 'category_new')