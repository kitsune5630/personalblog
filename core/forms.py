from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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
        widget=forms.TextInput, 
    )
    text = forms.CharField(
        max_length = 1000, min_length=10,
        label="Пост", help_text="Введите текст поста",
        widget=forms.Textarea,
    )