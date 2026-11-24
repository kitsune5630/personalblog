from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=25, min_length=5,
        label="Логин", help_text="Введите имя пользователя",
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=100, min_length=5,
        label="Пароль", help_text="Введите пароль"
    )
    email = forms.EmailField(
        max_length=100, min_length=5,
        label="Почта", help_text="Введите электронную почту"
    )

    # def clean_username(self):
    #     username = self.cleaned_data["username"].strip()
    #     if UserModel.objects.filter(username=username).exists():
    #         raise forms.ValidationError("Этот юзер занят")
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get("email", "").strip()
    #     if email and UserModel.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Этот почта занят")
    #     return email

# class CustomLoginForm(AuthenticationForm):
#     error_messages = {
#         'invalid_login': 'Неверный логин или пароль.'
#     }

# class UserForm(forms.Form):
#     username = forms.CharField(
#         label="Логин",
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#         label="Пароль",
#     )

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if not UserModel.objects.filter(username=username).exists():
    #         raise forms.ValidationError("Юзер не найден")
    #     return username

    # def clean_password(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     breakpoint()
    #     if username:
    #         user = UserModel.objects.filter(username=username).first()
    #         if user and not user.check_password(password):
    #             raise forms.ValidationError("Неверный пароль")
    #     return password