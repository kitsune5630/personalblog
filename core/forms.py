from django import forms

# put there code for html django structure
class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
    )

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        min_length=5
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=100, min_length=5,
    )