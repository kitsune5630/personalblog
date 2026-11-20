from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserForm, UserRegistrationForm

# Create your views here.
def home(request):
    """
    Поведение при запроса начальной (главной) страницы
    На данный момент заглушка (пустая)
    """
    return render(request, "home.html")

def registration(request):
    """
    Поведение при запросе страницы "Регистрация"
    На данный момент условная заглушка (в дальнейшем будет бд)
    """
    if request.method == "POST":
        user_registrationform = UserRegistrationForm(request.POST)
        if user_registrationform.is_valid():
            messages.success(request, "Вы успешно зарегистрированы")
            return redirect("success_registration")
    else:
        user_registrationform = UserRegistrationForm()
    context = {"form": user_registrationform}
    return render(request, "registration.html", context=context)

def success_registration(request):
    """
    Поведение при успешной регистрации
    """
    return render(request, "success_registration.html")

def login(request):
    """
    Поведение при запросе страницы "Вход"
    Вход под пользователем
    (на данный момент просто обработано поведение с ограничениями без бд)
    Очевидно, будет изменено на GET с БД
    """
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            # username = userform.cleaned_data["username"]
            # password = userform.cleaned_data["password"]
            messages.success(request, "Вы успешно авторизованы!")
            return redirect("success_login")
    else:
        userform = UserForm()
    context = {"form": userform}
    return render(request, "login.html", context=context)

def success_login(request):
    """
    Вывод страницы при успешном входе
    (на данный момент подлежит дальнейшему изменению, временная заглушка)
    """
    return render(request, "success_login.html")

def references(request):
    """
    Поведение при запросе страницы "Ссылки"
    """
    github_ref = "https://github.com/kitsune5630"
    leetcode_ref = "https://leetcode.com/u/kitsune12345/"
    data = {
        'github_ref' : github_ref,
        'leetcode_ref' : leetcode_ref,
    }
    return render(request, "references.html", context=data)

def about(request):
    """
    Поведение запроса страницы "Информация" / "Обо мне" (название пока первое)
    """
    context = {
        "personalphoto": "/static/images/personalphoto.png", 
        "name": "Иван", "lastname": "Иванов", "surname": "Иванович",
        "skills": [
            "Python", "Django", "HTML/CSS", 
            "GIT", "DOCKER", "REST API"
        ],
        "projects": [
            {"title": "Блог", "url": "https://github.com/kitsune5630/personalblog"},
        ],
        "education": {
            "image": "/static/images/Nstu.jpg", 
            "name": "Новосибирский Государственный Технический Университет",
            "shortname": "НГТУ",
            "speciality": "Программное обеспечение компьютерных систем и сетей",
            "course": "4",
        },
        "contact_info": {
            "telegram": "@kitsune5630",
            "telegram_url": "https://t.me/kitsune5630",
            "mail": "kitsune5630@proton.me"
        }
    }
    return render(request, "about.html", context=context)

