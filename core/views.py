from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm, PostCreationForm, CustomUserCreationform
from .models import PostsModel
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    """
    Поведение при запроса начальной (главной) страницы
    На данный момент заглушка (пустая)
    """

    # позже поменять на подсчет из бд
    context = {
        "count_users": User.objects.count(),
        "count_posts": PostsModel.objects.count(),
    }
    return render(request, "home.html", context=context)

def posts(request):
    """
    Страница со всеми имеющимися постами
    """
    posts_list = PostsModel.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { "posts": page_obj }
    return render(request, "posts.html", context=context)

def post_detail(request, slug):
    """
    Детали поста
    """
    post = get_object_or_404(PostsModel, slug=slug)
    return render(request, "post_detail.html", {"post": post})

# def post_detail(request, pk):
#     """
#     Детали поста
#     """
#     post = get_object_or_404(PostsModel, id=pk)

#     context = {
#         "post": post
#     }
#     return render(request, "post_detail.html", context=context)

def post_create(request):
    """
    Создание поста
    """
    if request.method == "POST":
        post_createform = PostCreationForm(request.POST)
        if post_createform.is_valid():
            title = post_createform.cleaned_data["title"]
            text = post_createform.cleaned_data["text"]
            author = request.user.username
            PostsModel.objects.create(
                title=title, text=text, author=author
            )
            messages.success(request, "Пост успешно создан!")
            return redirect("success_post_create")
    else:
        post_createform = PostCreationForm()
    context = {"form": post_createform }
    return render(request, "post_create.html", context=context)

def success_post_create(request):
    """
    Успешное создание поста
    """
    return render(request, "success_post_create.html")

def registration(request):
    """
    Поведение при запросе страницы "Регистрация"
    добавлена таблица для юзера с уникальными полями
    """
    if request.method == "POST":
        user_registrationform = CustomUserCreationform(request.POST)
        if user_registrationform.is_valid():
            user = user_registrationform.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрированы")
            return redirect("success_registration")
    else:
        user_registrationform = CustomUserCreationform()
    context = {"form": user_registrationform}
    return render(request, "registration.html", context=context)

def success_registration(request):
    """
    Поведение при успешной регистрации
    """
    return render(request, "success_registration.html")

def login_view(request):
    form = CustomAuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("success_login")
    return render(request, "registration/login.html", {'form': form})


# class MyLoginView(LoginView):
    """
    Кастом логин вьюха
    """
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm 

def success_login(request):
    """
    Вывод страницы при успешном входе
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
