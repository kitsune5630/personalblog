from django import forms

# put there code for html django structure
class UserForm(forms.Form):
    username = forms.CharField(
        label="Логин",
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль",
    )

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=25, min_length=5,
        label="Логин",
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=100, min_length=5,
        label="Пароль",
    )
    email = forms.EmailField(
        max_length=100, min_length=5,
        required=False, label="Почта",
    )