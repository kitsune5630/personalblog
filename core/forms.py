from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import CommentModel, PostsModel, TagsModel

class CustomUserCreationform(UserCreationForm):
    """
    Переопределение UserCreationForm
    """
    username = forms.CharField(
            max_length=25, min_length=5,
            label="Пользователь", help_text="Введите имя пользователя",
    )
    email = forms.EmailField(
            max_length=100, min_length=5,
            label="Почта", help_text="Введите электронную почту",
        )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Пароль подтвердить", widget=forms.PasswordInput,
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    """
    Изменение данных уже существующих полей формы AuthenticationForm
    """
    username = forms.CharField(
        label="Пользователь", 
        widget=forms.TextInput(attrs={'autofocus': True}),
        help_text="Введите имя пользователя",
    )
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput,
        help_text="Введите пароль", 
    )

class PostCreationForm(forms.Form):

    """
    Форма для создания поста
    """
    title = forms.CharField(
        max_length=100, min_length=5,
        label="Заголовок", help_text="Введите заголовок",
        widget=forms.TextInput
    )
    text = forms.CharField(
        max_length = 1000, min_length=10,
        label="Пост", help_text="Введите текст поста",
        widget=forms.Textarea,
    )

    tags_input = forms.CharField(
        required=False, 
        label="Теги", 
        help_text="Введите теги через пробел или запятую",
        widget=forms.TextInput(attrs={'placeholder': 'новый тег'})
    )

    class Meta:
        model = PostsModel
        fields = ['title', 'text'] 

class ProfileCreationForm(forms.Form):
    phone_number = forms.CharField(
        max_length=20, label="Номер телефона",
        help_text="Введите номер телефона", required=False,
        widget=forms.TextInput,
    )
    telegram = forms.CharField(
        max_length=20, label="Телеграм",
        help_text="Введите телеграм", required=False,
        widget=forms.TextInput,
    )
    about_self = forms.CharField(
        max_length=1000, label="О себе",
        help_text="Напишите о себе", required=False, 
        widget=forms.Textarea,
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']
        widgets = {
            "text": forms.Textarea(attrs={'rows':3, 'placeholder': 'Ваш комментарий...'}),
        }
        labels = {'text': 'комментарий'}

class SearchForm(forms.Form):
    title = forms.CharField(required=False, label="Заголовок")
    author = forms.CharField(required=False, label="Автор")
    tag = forms.ModelChoiceField(
        queryset=TagsModel.objects.all(),
        required=False, empty_label="ALL tags",
        label="Теги"
    )
    