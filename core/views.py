from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """
    Поведение при запроса начальной (главной) страницы
    На данный момент заглушка (пустая)
    """
    # posts = [
    #     {
    #         "article": "Название 1",
    #         "date": "01.01.2001",
    #         "author": "Ivan Ivanov",
    #         "text": "Minim reprehenderit labore veniam dolor commodo anim adipisicing sint nostrud in."
    #     },
    #     {
    #         "article": "Название 2",
    #         "date": "02.01.2001",
    #         "author": "Ivan Ivanov",
    #         "text": "Minim reprehenderit labore veniam dolor commodo anim adipisicing sint nostrud in."
    #     },
    # ]

    # позже поменять на подсчет из бд
    context = {
        "count_users": 2,
        "count_posts": 3,
    }
    return render(request, "home.html", context=context)

def posts(request):
    """
    Заглушка для страницы с постами
    """
    return render(request, "posts.html")

def post_detail(request):
    """
    Временная заглушка-шаблон до бд
    """
    post = {
        "article": "Название 1",
        "date": "01.01.2001",
        "author": "Ivan Ivanov",
        "text": "Minim reprehenderit labore veniam dolor commodo anim adipisicing sint nostrud in."
    }

    context = {
        "post": post
    }
    return render(request, "post.html", context=context)

def post_create(request):
    """
    Заготовка для создания поста
    """
    return render(request, "post_create.html")

def registration(request):
    """
    Поведение при запросе страницы "Регистрация"
    добавлена таблица для юзера с уникальными полями
    """
    if request.method == "POST":
        user_registrationform = UserRegistrationForm(request.POST)
        if user_registrationform.is_valid():
            username = user_registrationform.cleaned_data["username"]
            password = user_registrationform.cleaned_data["password"]
            email = user_registrationform.cleaned_data["email"]
            email 
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
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
    Для кастом имени accounts/login
    """
    return render(request, 'login.html')

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

# def login(request):
#     """
#     Поведение при запросе страницы "Вход"
#     Вход под пользователем
#     (на данный момент просто обработано поведение с ограничениями без бд)
#     Очевидно, будет изменено на GET с БД
#     """
#     if request.method == "POST":
#         user_login = UserForm(request.POST)
#         if user_login.is_valid():
#             username = user_login.cleaned_data["username"]
#             user = User.objects.filter(username=username).exists()
#             if not user:
#                 user_login.add_error("username", "Юзер не найден")
#             else:
#                 password = user_login.cleaned_data["password"]
#                 user1 = authenticate(request, username=username, password=password)
#                 if user1 is not None:
#                     login(request, user1)
#                     messages.success(request, "Вы успешно авторизованы!")
#                     return redirect('success_login')
#                 else:
#                     user_login.add_error("password", "Пароль не найден")
#     else:
#         user_login = UserForm()
#     context = {"form": user_login}
#     return render(request, "login.html")