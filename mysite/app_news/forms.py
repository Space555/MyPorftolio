from django import forms
from app_news.models import News, Category, Comment


class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=300, label='Заголовок', widget=forms.TextInput(attrs={'class': 'create__form-input', 'placeholder': 'Введите название *'}))
    descr = forms.CharField(label='Новость', widget=forms.Textarea(attrs={'class': 'create__form-textarea', 'placeholder': 'Введите текст *'}))
    link_new = forms.CharField(label='Ссылка на новость', widget=forms.TextInput(attrs={'class': 'create__form-input', 'placeholder': 'Ссылка *'}), max_length=500)
    sourse_new = forms.CharField(label='Источник новости', widget=forms.TextInput(attrs={'class': 'create__form-input', 'placeholder': 'Источник *'}), max_length=500)
    category_new = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберете категорию', label='Категория')
    image = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'фото поста'}),required=False)
    class Meta:
        model = News
        fields = ('title', 'descr', 'link_new', 'sourse_new', 'category_new', 'image')


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment-text'}))

    class Meta:
        model = Comment
        fields = ('text',)