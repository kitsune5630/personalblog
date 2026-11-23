from django import forms
from .models import UserModel

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

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if UserModel.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот юзер занят")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()
        if email and UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот почта занят")
        return email